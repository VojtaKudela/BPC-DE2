#ifndef SOIL_H
# define SOIL_H

/* 
 * GPIO library for AVR-GCC.
 * (c) 2024 Vojtech Kudela, MIT license
 *
 */

/**
 * @file 
 * @defgroup kudela_soil GPIO Library <soil.h>
 * @code #include <soil.h> @endcode
 *
 * @brief Valve regulation library for AVR-GCC.
 *
 * The library contains functions for controlling AVRs' valve
 * using GPIO.
 *
 * @note Based on AVR Libc Reference Manual.
 * @copyright (c) 2024 Vojtech Kudela, MIT license
 * @{
 */

// -- Includes -------------------------------------------------------
#include <avr/io.h>


// -- Function prototypes --------------------------------------------
/**
 * @brief  Initialize valve pin, switch valve off.
 * @par    Implementation notes:
 *           - Connect transistor to selected pin.
 *           - Transistor will switch valve via relay.
 *           - Connect diode parallel to relay.
 *           - External pull-up is necessary.
 *           - Connect a resistor to the base of transistor
 *           - to limit the current.
 * @param  reg Address of Port Register, such as &PORTB.
 * @param  pin Pin designation in the interval 0 to 7.
 * @return none
 */
void SOIL_init(volatile uint8_t *reg, uint8_t pin);


/**
 * @brief  Turn valve on.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.  
 * @return Set bit 0 to one.
 */
uint8_t SOIL_on(volatile uint8_t *reg, uint8_t pin);


/**
 * @brief  Turn valve off.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.  
 * @return Set bit 0 to zero.
 */
uint8_t SOIL_off(volatile uint8_t *reg, uint8_t pin);


/**
 * @brief  Control valve.
 * @param  soil_reg      Valve, address of Port Register, such as &PORTB.
 * @param  soil_pin      Valve, pin designation in the interval 0 to 7.
 * @param  current_soil  Measured soil moisure value.
 * @param  setpoint_soil Required soil moisurevalue.
 * @param  hyst_soil     Hysteresis of soil moisure
 * @return None
 * @details Minimum value is required value minus hysteresis. Required value is typical value.
 *          Valve is turn on, if soil moisure is lower than minimum value or if soil moisure
 *          is lower than typical value and valve was turn on.
 */
void SOIL_control(volatile uint8_t *soil_reg, uint8_t soil_pin, uint8_t current_soil, uint8_t setpoint_soil, uint8_t hyst_soil);
/** @} */

#endif