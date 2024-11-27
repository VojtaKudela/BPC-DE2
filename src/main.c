
// Includes
#include <avr/io.h>
#include <avr/interrupt.h>
#include <uart.h>
#include <timer.h>
#include <util/twi.h>
#include <twi.h>
#include <adc.h>

// For debug
#include <stdlib.h>         // C library. Needed for number conversions

#ifndef F_CPU
# define F_CPU 16000000  // CPU frequency in Hz required for UART_BAUD_SELECT
#endif

// RTC Definitions
#define RTC_ADR 0x68
#define RTC_SEC_MEM 0x00
#define RTC_MIN_MEM 0x01
#define RTC_HOUR_MEM 0x02
#define RTC_DAY_MEM 0x03
#define RTC_DATE_MEM 0x04
#define RTC_MONTH_MEM 0x05
#define RTC_YEAR_MEM 0x06

// DHT Sensor Definitions
#define DHT_ADR 0x5c
#define DHT_HUM_MEM 0
#define DHT_TEMP_MEM 2

// UART definition
#define BAUDRATE 9600

// Global variables
volatile uint8_t update_data = 0;

struct data_packet {
   volatile uint8_t year;
   volatile uint8_t month;
   volatile uint8_t date;
   volatile uint8_t day;
   volatile uint8_t hour;
   volatile uint8_t minute;
   volatile uint8_t second;
   volatile uint8_t hum_int;
   volatile uint8_t hum_dec;
   volatile uint8_t temp_int;
   volatile uint8_t temp_dec;
   volatile uint16_t lux;
   volatile uint16_t soil;
   volatile uint8_t mask;
} dp;

struct rec_time {
   volatile uint8_t year;
   volatile uint8_t month;
   volatile uint8_t date;
   volatile uint8_t day;
   volatile uint8_t hour;
   volatile uint8_t minute;
   volatile uint8_t second;
} rc;

struct rec_reg {
   volatile uint8_t temp_val;
   volatile uint8_t temp_hys;
   volatile uint8_t hum_val;
   volatile uint8_t hum_hys;
   volatile uint8_t soil_val;
   volatile uint8_t soil_hys;
   volatile uint8_t ilu_100;
   volatile uint8_t ilu_1;
} rg;

// Startup
void startup(void)
{
    dp.mask = '\n';

    uart_init(UART_BAUD_SELECT(BAUDRATE, F_CPU));
    twi_init();

    // Main clock
    TIM1_ovf_1sec();
    TIM1_ovf_enable();

    // ADC clock
    TIM2_ovf_16ms();
    TIM2_ovf_enable();

    ADC_setup();

    sei();
}

void write_rtc_data(void)
{
    twi_start();

    if (twi_write((RTC_ADR<<1) | TWI_WRITE) == 0) // RTC I2C address
    {   
        twi_write(RTC_SEC_MEM);         // Register to start reading
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

void read_rtc_data(void)
{
    twi_start();
    if (twi_write((RTC_ADR<<1) | TWI_WRITE) == 0) 
    {
        twi_write(RTC_SEC_MEM);
        twi_stop();

        twi_start();
        twi_write((RTC_ADR<<1) | TWI_READ);
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

// DHT Sensor Functions
void read_dht_data(void)
{
    uint8_t hum_raw[2], temp_raw[2];
    uint8_t cumsum;
    
    twi_start();

    if (twi_write((DHT_ADR<<1) | TWI_WRITE) == 0) // Start communication with DHT
    {
        twi_write(DHT_HUM_MEM);                   // Point to humidity register
        twi_stop();

        twi_start();
        twi_write((DHT_ADR << 1) | TWI_READ);    // Read operation
        hum_raw[0] = twi_read(TWI_ACK);          // Read high byte of humidity
        hum_raw[1] = twi_read(TWI_ACK);          // Read low byte of humidity
        temp_raw[0] = twi_read(TWI_ACK);         // Read high byte of temperature
        temp_raw[1] = twi_read(TWI_ACK);         // Read low byte of temperature
        cumsum      = twi_read(TWI_NACK);        // Read cumsum
        
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

// Main loop
int main(void)
{
    uint8_t lux_rec;
    uint8_t soil_rec;

    uint8_t new_data;  // Carry information about type of new data 0 - none, 1 - reg, 2 - time
    uint16_t uart_data; // Receive uart_byte
    uint8_t data_count;// Number of receive bytes

    startup();

    while (1)
    {
        uart_data = uart_getc();

        if ((uart_data>>8)==0)
        {
            uart_data = (uart_data&0x00ff);

            // First letter carry information about type of data
            if (new_data == 0)
            {
                if (uart_data == 'T')
                {
                    new_data = 2;
                    data_count++;
                }
                else if (uart_data == 'R')
                {
                    new_data = 1;
                    data_count++;
                }
            }
            // Receive regulation data
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
                    
                data_count++;
                
            }
             // Receive time data
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
                data_count++;
            }
             
            if ((new_data == 1) & (data_count > 8))
            {
                data_count = 0;
                new_data = 0;

            }
            // Apply time value
            else if ((new_data == 2) & (data_count > 7))
            {
                data_count = 0;
                new_data = 0;
                write_rtc_data();  // Data are send via I2C
            }
        }

        if (update_data == 1)
        {
            // Read RTC and DHT data
            read_rtc_data();
            read_dht_data();

            // Preper transmit value
            lux_rec = dp.lux>>2;
            soil_rec = dp.soil>>2;

            // Check mask conditions for lux and soil
            if (lux_rec == dp.mask)
                lux_rec += 1;

            if (soil_rec == dp.mask)
                soil_rec += 1;

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
            uart_putc(soil_rec);
            uart_putc(lux_rec);
            uart_putc(dp.mask);
            update_data = 0;

/*
            itoa(dp.year, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.month, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.date, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.day, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.hour, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.minute, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.second, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.temp_int, string, 10);
            uart_puts(string);
            uart_putc('.');
            itoa(dp.temp_dec, string, 10);
            uart_puts(string);
            uart_puts(" ");
            itoa(dp.hum_int, string, 10);
            uart_puts(string);
            uart_putc('.');
            itoa(dp.hum_dec, string, 10);
            uart_puts(string);
            uart_putc(' ');
            itoa(dp.soil, string, 10);
            uart_puts(string);
            uart_putc(' ');
            itoa(dp.lux, string, 10);
            uart_puts(string);
            uart_puts("\r\n");
            */
        }
    }

    return 0;
}

ISR(TIMER1_OVF_vect)
{
    update_data = 1;
}

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

ISR(ADC_vect)
{
    if (ADMUX & (1 << MUX0)) 
    {
        dp.soil = ADC; // Connect to A3
    } 
        else 
    {
        dp.lux = ADC; // Connect to A2
    }
}