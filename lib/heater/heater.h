#ifndef HEATER_H
# define HEATER_H

/* 
 * GPIO library for AVR-GCC.
 * (c) 2019-2024 Tomas Fryza, MIT license
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

/**
 * @file 
 * @defgroup fryza_gpio GPIO Library <gpio.h>
 * @code #include <gpio.h> @endcode
 *
 * @brief GPIO library for AVR-GCC.
 *
 * The library contains functions for controlling AVRs' gpio pin(s).
 *
 * @note Based on AVR Libc Reference Manual.
 * @copyright (c) 2019-2024 Tomas Fryza, MIT license
 * @{
 */

// -- Includes -------------------------------------------------------
#include <avr/io.h>


// -- Function prototypes --------------------------------------------
/**
*/
void HEATER_init(volatile uint8_t *reg, uint8_t pin);


/**
 */
void FAN_init(volatile uint8_t *reg, uint8_t pin);

/**
 */
void INH_init(volatile uint8_t *reg, uint8_t pin);

/**
 */
void HEATER_on(volatile uint8_t *reg, uint8_t pin);


/**
 */
void HEATER_off(volatile uint8_t *reg, uint8_t pin);


/**
 */
void FAN_on(volatile uint8_t *reg, uint8_t pin);


/**
 */
void FAN_off(volatile uint8_t *reg, uint8_t pin);


/**
 */
void INH_on(volatile uint8_t *reg, uint8_t pin);


/**
 */
void INH_off(volatile uint8_t *reg, uint8_t pin);

/**
 */

void HEATER_FAN_control(volatile uint8_t *heater_reg, uint8_t heater_pin, volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, int8_t current_temp, int8_t setpoint_temp, int8_t hyst_temp, int8_t current_hum, int8_t setpoint_hum, int8_t hyst_hum);
/** @} */

#endif