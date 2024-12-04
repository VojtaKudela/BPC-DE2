#ifndef PD_H
# define PD_H
/* 
 * Preper_data libary
 * (c) Antonin_Putala 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

/**
 * @file 
 * @defgroup Preper_data library <preper_data.h>
 * @code #include <preper_data.h> @endcode
 *
 * @brief Preper data for Tropical plants.
 *
 * The library contains functions for prepering data.
 *
 * @copyright (c) Antonin Putala 2024
 * @{
 */

/* Includes -----------------------------------------------*/
#include <avr/io.h>

/* Function prototypes ------------------------------------*/
/**
 * @brief  Rounded number with decimal and integer part.
 * @param  int_part Integer part of number.
 * @param  dec_part Decimal part of number.
 * @return Rounded value
 */
uint8_t PD_round(uint8_t int_part, uint8_t dec_part);

/**
 * @brief  Prepered illumination and soil moisure for transmission.
 * @param  value 10-bit output ADC
 * @param  mask  Forbidden value
 * @return 8-bit data prepered for UART
 */
uint8_t PD_uart(uint16_t value, uint8_t mask);

/**
 * @brief  Calculate the illumination value.
 * @param  value 16-bit, output of ADC
 * @return 16-bit, sensible value of illumination
 */
uint16_t PD_ilu(uint16_t value);

/**
 * @brief  Calculate the soil moisure value.
 * @param  value 16-bit, output of ADC
 * @return 8-bit, sensible value of soil moisure
 */
uint8_t PD_soil(uint16_t value);

/** @} */
#endif