#ifndef TROPICAL_DEF_H
# define TROPICAL_DEF_H

/***********************************************************
 * 
 * Definitions for the Tropical plants project.
 * (c) 2024 Antonin Putala, MIT license
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 *
 ***********************************************************/

/**
 * @file 
 * @defgroup putala_trop Timer Library <tropical_def.h>
 * @code #include <tropical_def.h> @endcode
 *
 * @brief Definitions for the Tropical plants project.
 *
 * The file contains declarations of functions, data 
 * structures, and necessary definitions for the Tropicla plants project.
 *
 * @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 *         of Technology, Czechia
 * @copyright (c) 2024 Antonin Putala, This work is licensed under 
 *                the terms of the MIT license
 * @{
 */

/** @brief CPU frequency in Hz required for UART_BAUD_SELECT. */
#ifndef F_CPU
# define F_CPU 16000000  
#endif


/* Defines ------------------------------------------------*/
/**
 * @name  Definitions for Tropical plants.
 */
/** @brief I2C real-time clock address. */
#define RTC_ADR 0x68

/** @brief RTC memory addresses. */
#define RTC_SEC_MEM 0x00
#define RTC_MIN_MEM 0x01
#define RTC_HOUR_MEM 0x02
#define RTC_DAY_MEM 0x03
#define RTC_DATE_MEM 0x04
#define RTC_MONTH_MEM 0x05
#define RTC_YEAR_MEM 0x06

/** @brief I2C address of the combined humidity and temperature sensor. */
#define DHT_ADR 0x5c

/** @brief DHT memory addresses. */
#define DHT_HUM_MEM 0
#define DHT_TEMP_MEM 2

/** @brief Definition of UART baudrate. */
#define BAUDRATE 9600

/* Function prototypes ------------------------------------*/
/**
 * @brief   Initialization of peripherals.
 * @param   None
 * @return  None
 * @details Sets the last character of the transmitted strings. 
 * Sets the default values ​​of the control register. Initializes 
 * the heater, fan, valve and inhaler. Initializes TWI, UART and 
 * ADC. Sets PWM. Sets the interrupts of timers 1 and 2. Enables 
 * interrupts.
 */
void startup(void);

/**
 * @brief   Sets the real-time clock value.
 * @param   None
 * @return  None
 * @details Sends a write request. The first byte 
 *          is the address of the memory to be overwritten. 
 *          This is followed by a total of 7 bytes with 
 *          the values ​​of the memory in which the time 
 *          is stored.
 */
void write_rtc_data(void);

/**
 * @brief   Reads data from the real-time clock.
 * @param   None
 * @return  None
 * @note    If hum_int + temp_int + (hum_dec + temp_dec)/10 is not cumsum,
 *          data are not overwriten.
 * @details Communication is via I2C. In the 
 *          first step, a request is sent to write 
 *          to the combined humidity and temperature sensor 
 *          with the memory address. Then a request is sent 
 *          to read. The contents of all 5 memories are read: 
 *          hum_int, hum_dec, temp_int, temp_dec, cumsum.
 */
void read_rtc_data(void);

/** 
 * @brief   Reads data from the combined humidity and temperature sensor.
 * @param   None
 * @return  None
 * @details Communication is via I2C. In the 
 *          first step, a request is sent to write 
 *          to the real-time clock with the memory address. 
 *          Then a request is sent to read. The contents of 
 *          the first 7 memories are read: seconds, minutes, 
 *          hours, days of the week, date, month and year.
 */
void read_dht_data(void);

/**
 * @brief  Sends measured values ​​via UART.
 * @param  None
 * @return None
 */
void transmit_uart_data(void);

/* Global variables -----------------------------------*/
/** @brief Data packet. Data are prepared to transmit. */
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

/** @brief Received data from UART, time settings. */
struct rec_time {
   volatile uint8_t year;
   volatile uint8_t month;
   volatile uint8_t date;
   volatile uint8_t day;
   volatile uint8_t hour;
   volatile uint8_t minute;
   volatile uint8_t second;
} rc;

/** @brief Received data from UART, control of quantities. */
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

#endif

/** @} */