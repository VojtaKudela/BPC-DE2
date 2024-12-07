/* 
 * Tropical plants library
 * (c) Vit Janos, Jakub Kupcik, Vojtech Kudela, Antonin Putala 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 * Tested by SimulIDE.
 */

/**
 * @mainpage Tropical plants
 *
 * Tropical plants is a firmware for the AVR microcontroller. It 
 * allows you to measure temperature, humidity, soil moisture and 
 * illumination in the greenhouse in real time. It also allows you 
 * to regulate these quantities at a set value. It allows communication 
 * with a PC via a serial port.
 *
 * @author    Vit Janos, Jakub Kupcik, Vojtech Kudela, Antonin Putala, 
 *            Dept. of Radio Electronics, Brno University of Technology, Czechia
 * @copyright (c) 2024 Vit Janos, Jakub Kupcik, Vojtech Kudela, Antonin Putala, 
 *            This work is licensed under the terms of the MIT license
 */

// -- Includes -------------------------------------------------------
#include <avr/io.h>            // Contains pin and register names.
#include <avr/interrupt.h>     // Contains interrupt functions.
#include <uart.h>              // UART handling library by Peter Fleury.
#include <timer.h>             // Timer library for AVR-GCC
#include <util/twi.h>          
#include <twi.h>               // I2C/TWI library for AVR-GCC
#include <adc.h>               // ADC library for AVR-GCC
#include <heater.h>            // Heater, fan and inhalator handling library
#include <soil.h>              // Valve handling library
#include <pwm.h>               // PWM library for AVR-GCC
#include <preper_data.h>       // Auxiliary function for the Tropical Plants project
#include <tropical_def.h>      // Contain necessary defines and function declarations



// -- Defines -------------------------------------------------------
// Regulation pins
#define HEAT PB0
#define COOL PB1
#define INHA PB2
#define VALV PB3

// Regulation port
#define REG_PORT &PORTB

// -- Global variables  ----------------------------------------------
volatile uint8_t update_data = 0;

// -- Function definitions -------------------------------------------
/*
 * Function: startup
 * Purpose:  Initialization of peripherals.
 * Input(s): None
 * Returns:  None
 */
void startup(void)
{
    // Last transmitted symbol
    dp.mask = '\n';

    uart_init(UART_BAUD_SELECT(BAUDRATE, F_CPU));
    twi_init();

    // Initialize regulation pin
    HEATER_init(REG_PORT-1, HEAT); // address of PORT - 1 is adress of DDR
    FAN_init(REG_PORT-1, COOL);
    INH_init(REG_PORT-1, INHA);
    SOIL_init(REG_PORT-1, VALV);

    // Initialization of PWM
    PWM_enable();
    PWM_set_duty(0);

    // Default data of the regulatory repository
    rg.temp_val = 25;
    rg.temp_hys = 2;
    rg.hum_val = 50;
    rg.hum_hys = 5;
    rg.soil_val = 50;
    rg.soil_hys = 5;
    rg.ilu_100 = 1;
    rg.ilu_1 = 0;

    // Main clock
    TIM1_ovf_1sec();
    TIM1_ovf_enable();

    // ADC clock
    TIM2_ovf_16ms();
    TIM2_ovf_enable();

    // ADC initialization
    ADC_setup();

    // Global interrupt enable
    sei();
}

/*
 * Function: write_rtc_data
 * Purpose:  Sets the real-time clock value.
 * Input(s): None
 * Returns:  None
 */
void write_rtc_data(void)
{
    twi_start();

    // RTC I2C address
    if (twi_write((RTC_ADR<<1) | TWI_WRITE) == 0) 
    {   
        // Register to start writing
        twi_write(RTC_SEC_MEM); 

        // Writing data to memory        
        twi_write(rc.second); 
        twi_write(rc.minute); 
        twi_write(rc.hour); 
        twi_write(rc.day);
        twi_write(rc.date);
        twi_write(rc.month);
        twi_write(rc.year);
    }

    twi_stop();
}

/*
 * Function: read_rtc_data
 * Purpose:  Reads data from the real-time clock.
 * Input(s): None
 * Returns:  None
 */
void read_rtc_data(void)
{
    twi_start();

    // RTC I2C address
    if (twi_write((RTC_ADR<<1) | TWI_WRITE) == 0) 
    {
        // Register to start reading
        twi_write(RTC_SEC_MEM);
        twi_stop();

        // Repeated start
        twi_start();
        twi_write((RTC_ADR<<1) | TWI_READ);

        // Reading data from memory   
        dp.second = twi_read(TWI_ACK);
        dp.minute = twi_read(TWI_ACK);
        dp.hour = twi_read(TWI_ACK);
        dp.day = twi_read(TWI_ACK);
        dp.date = twi_read(TWI_ACK);
        dp.month = twi_read(TWI_ACK);
        dp.year = twi_read(TWI_NACK);
    }

    twi_stop();
}

/*
 * Function: read_dht_data
 * Purpose:  Reads data from the combined humidity and temperature sensor.
 * Input(s): None
 * Returns:  None
 */
void read_dht_data(void)
{
    // Temporary storage of the read values
    uint8_t hum_raw[2], temp_raw[2];
    uint8_t cumsum;
    
    twi_start();

    // DTH I2C address
    if (twi_write((DHT_ADR<<1) | TWI_WRITE) == 0) // Start communication with DHT
    {
        twi_write(DHT_HUM_MEM);                   // Point to humidity register
        twi_stop();

        // Repeated start
        twi_start();
        twi_write((DHT_ADR << 1) | TWI_READ);     // Read operation
        hum_raw[0] = twi_read(TWI_ACK);           // Read high byte of humidity
        hum_raw[1] = twi_read(TWI_ACK);           // Read low byte of humidity
        temp_raw[0] = twi_read(TWI_ACK);          // Read high byte of temperature
        temp_raw[1] = twi_read(TWI_ACK);          // Read low byte of temperature
        cumsum      = twi_read(TWI_NACK);         // Read cumsum
        
        // Are received data correct?
        if ((hum_raw[1] + temp_raw[1] + hum_raw[0] + temp_raw[0]) == cumsum)                                    
        {
            dp.hum_int = hum_raw[0];
            dp.hum_dec = hum_raw[1];
            dp.temp_int = temp_raw[0];
            dp.temp_dec = temp_raw[1];
        }
    }

    twi_stop();

}

/*
 * Function: transmit_uart_data
 * Purpose:  Sends measured values ​​via UART.
 * Input(s): None
 * Returns:  None
 */
void transmit_uart_data(void)
{
    // Local variables, modified values ​​for sending
    uint8_t lux_rec;
    uint8_t soil_rec;

    // Preper transmit value
    lux_rec = PD_uart(dp.lux,dp.mask);
    soil_rec = PD_uart(dp.soil,dp.mask);

    // Send updated data via UART
    uart_putc(dp.year);
    uart_putc(dp.month);
    uart_putc(dp.date);
    uart_putc(dp.day);
    uart_putc(dp.hour);
    uart_putc(dp.minute);
    uart_putc(dp.second);
    uart_putc(dp.hum_int);
    uart_putc(dp.hum_dec);
    uart_putc(dp.temp_int);
    uart_putc(dp.temp_dec);
    uart_putc(lux_rec);
    uart_putc(soil_rec);
    uart_putc(dp.mask);

    // Update checked
    update_data = 0; 
}

// Main loop
int main(void)
{
    uint16_t ilu_set;    // The lighting control level will be stored here.
    uint8_t  new_data;   // Carry information about type of new data 0 - none, 1 - reg, 2 - time
    uint8_t  data_count; // Number of receive bytes
    uint16_t uart_data;  // Receive uart_byte

    // Initialization
    startup();

    // Forever loop
    while (1)
    {
        // Obtaining data from serial communication.
        uart_data = uart_getc();

        if ((uart_data>>8)==0)
        {
            // Only the lower byte contains data.
            uart_data = (uart_data&0x00ff);

            // First letter carry information about type of data
            if (new_data == 0)
            {

                // The data packet with the time setting starts with the ASCII character T.
                if (uart_data == 'T')
                {
                    // Ready to receive time data packet.
                    new_data = 2;
                    data_count++;
                }

                // The data packet with the regulation setting starts with the ASCII character R.
                else if (uart_data == 'R')
                {
                    
                    // Ready to receive regulation data packet.
                    new_data = 1;
                    data_count++;
                }
            }

            // Receive regulation data.
            // Data on the serial line has a strict order.
            else if (new_data == 1)
            {
                switch (data_count)
                    {
                        case 1:
                            rg.temp_val = uart_data;
                            break;
                        case 2:
                            rg.temp_hys = uart_data;
                            break;
                        case 3:
                            rg.hum_val = uart_data;
                            break;
                        case 4:
                            rg.hum_hys = uart_data;
                            break;
                        case 5:
                            rg.soil_val = uart_data;
                            break;
                        case 6:
                            rg.soil_hys = uart_data;
                            break;
                        case 7:
                            rg.ilu_100 = uart_data;
                            break;
                        default:
                            rg.ilu_1 = uart_data;
                            break;
                    }
                
                // Ready to process another byte.
                data_count++;
                
            }

            // Receive time data.
            // Data on the serial line has a strict order.
            else if (new_data == 2)
            {
                    switch (data_count)
                    {
                        case 1:
                            rc.year = uart_data;
                            break;
                        case 2:
                            rc.month = uart_data;
                            break;
                        case 3:
                            rc.date = uart_data;
                            break;
                        case 4:
                            rc.day = uart_data;
                            break;
                        case 5:
                            rc.hour = uart_data;
                            break;
                        case 6:
                            rc.minute = uart_data;
                            break;
                        default:
                            rc.second = uart_data;
                            break;
                    }

                // Ready to process another byte.
                data_count++;
            }
            
            // Apply regulation value
            if ((new_data == 1) & (data_count > 8))
            {
                data_count = 0;   // Ready for the next reception.
                new_data = 0;     // Nothing is received.

            }
            // Apply time value
            else if ((new_data == 2) & (data_count > 7))
            {
                data_count = 0;    // Ready for the next reception.
                new_data = 0;      // Nothing is received.
                write_rtc_data();  // Data are send via I2C
            }
        }

        // After TIMER1 overflows.
        if (update_data == 1)
        {
            // Read RTC and DHT data
            read_rtc_data();
            read_dht_data();

            // Control of PWM
            ilu_set = rg.ilu_100*100 + rg.ilu_1;
            PWM_control(PD_ilu(dp.lux),ilu_set,10);

            // Control ventil
            SOIL_control(REG_PORT, VALV, PD_soil(dp.soil), rg.soil_val, rg.soil_hys);

            // Control heater, fan and inhalator
            HEATER_FAN_control(REG_PORT, HEAT, REG_PORT, COOL, REG_PORT, INHA, PD_round(dp.temp_int,dp.temp_dec), 
                                rg.temp_val, rg.temp_hys, PD_round(dp.hum_int,dp.hum_dec), rg.hum_val, rg.hum_hys);

            // Send updated data via UART
            transmit_uart_data();
        }
    }

    // It will never happen.
    return 0;
}

// Handling timer 1 interrupt triggers the update.
ISR(TIMER1_OVF_vect)
{
    update_data = 1;
}

// The timer 2 interrupt handler switches the ADC input 
// every fourth cycle and starts the conversion.
ISR(TIMER2_OVF_vect)
{
    static uint8_t counter = 0;
    counter++;

    if (counter >= 6) 
    {
        counter = 0;
        ADC_switchport();
        ADC_startconversion();
    }
}

// According to the multiplexer settings, the ADC saves
// the read value to the appropriate directory.
ISR(ADC_vect)
{
    if (ADMUX & (1 << MUX0)) 
    {
        dp.soil = ADC; // Connect to A3
    } 
        else 
    {
        dp.lux = ADC;  // Connect to A2
    }
}
