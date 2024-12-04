#ifndef ADC_H
# define ADC_H

/***********************************************************
 * 
 * Timer library for AVR-GCC.
 * (c) 2024 Jakub Kupcik, MIT license
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 *
 ***********************************************************/

/**
 * @file 
 * @defgroup kupcik_adc ADC Library <adc.h>
 * @code #include <adc.h> @endcode
 *
 * @brief Timer library for AVR-GCC.
 *
 * The library contains macros for controlling the adc modules.
 *
 * @note Based on Microchip Atmel ATmega328P manual and no source file
 *       is needed for the library.
 * @author Jakub Kupcik, Dept. of Radio Electronics, Brno University 
 *         of Technology, Czechia
 * @copyright (c) 2024 Jakub Kupcik, This work is licensed under 
 *                the terms of the MIT license
 * @{
 */

/* Defines ------------------------------------------------*/
/**
 * @name  Definitions for ADC.
 * @note  ADC can switch between analog pin 2 and pin 3.
 */
/** @brief Start conversion*/
#define ADC_startconversion() ADCSRA |= (1 << ADSC);

/** @brief   Initializate ADC .
 *  @details Multiplexer is defaultly set to analog pin 2.
*/
#define ADC_setup() \
    (ADCSRA |= (1 << ADPS2) | (1 << ADPS1)); \
    (ADMUX |= (1 << REFS0) | (1 << MUX1));   \
    (ADMUX &= ~((1 << MUX0) | (1 << MUX2) | (1 << MUX3))); \
    (ADCSRA |= (1 << ADEN) | (1 << ADIE));

/** @brief Switch between analog pin 2 and 3 */
#define ADC_switchport() ADMUX ^= (1 << MUX0);

/** @} */
#endif
