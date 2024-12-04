#ifndef HEATER_H
# define HEATER_H

/* 
 * Heater, fan and inhalator regulation library for AVR-GCC.
 * (c) 2024 Vojtech Kudela, Antonin Putala, MIT license
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 * Tested using Simulide.
 */

/**
 * @file 
 * @defgroup kudela_heater GPIO Library <heater.h>
 * @code #include <heater.h> @endcode
 *
 * @brief Heater, fan and inhalator regulation library for AVR-GCC.
 *
 * The library contains functions for controlling AVRs' heater, fan and
 * inhalator using GPIO.
 *
 * @note Based on AVR Libc Reference Manual.
 * @copyright (c) 2024 Vojtech Kudela, Antonin Putala, MIT license
 * @{
 */

// -- Includes -------------------------------------------------------
#include <avr/io.h>

// -- Defines --------------------------------------------------------
/**
 * @name Definition of ports and pins
 */
#define HEAT_BIT 0
#define FAN_BIT  1
#define INH_BIT  2

// -- Function prototypes --------------------------------------------
/**
 * @brief  Initialize heater pin, switch heater off.
 * @par    Implementation notes:
 *           - Connect transistor to selected pin.
 *           - Transistor will switch heater via relay.
 *           - Connect diode parallel to relay.
 *           - External pull-up is necessary.
 *           - Connect a resistor to the base of transistor
 *           - to limit the current.
 * @param  reg Address of Port Register, such as &PORTB.
 * @param  pin Pin designation in the interval 0 to 7.
 * @return none
 */
void HEATER_init(volatile uint8_t *reg, uint8_t pin);


/**
 * @brief  Initialize fan pin, switch fan off.
 * @par    Implementation notes:
 *           - Connect transistor to selected pin.
 *           - Transistor will switch fan via relay.
 *           - Connect diode parallel to relay.
 *           - External pull-up is necessary.
 *           - Connect a resistor to the base of transistor
 *           - to limit the current.
 * @param  reg Address of Port Register, such as &PORTB.
 * @param  pin Pin designation in the interval 0 to 7.
 * @return none
 */
void FAN_init(volatile uint8_t *reg, uint8_t pin);

/**
 * @brief  Initialize inhalator pin, switch inhalator off.
 * @par    Implementation notes:
 *           - Connect transistor to selected pin.
 *           - Transistor will switch inhalator via relay.
 *           - Connect diode parallel to relay.
 *           - External pull-up is necessary.
 *           - Connect a resistor to the base of transistor
 *           - to limit the current.
 * @param  reg Address of Port Register, such as &PORTB.
 * @param  pin Pin designation in the interval 0 to 7.
 * @return none
 */
void INH_init(volatile uint8_t *reg, uint8_t pin);

/**
 * @brief  Switch heater on.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 0 to one.
 */
uint8_t HEATER_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);


/**
 * @brief  Switch heater off.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 0 to zero.
 */
uint8_t HEATER_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);


/**
 * @brief  Switch fan on.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 1 to one.
 */
uint8_t FAN_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);


/**
 * @brief  Switch fan off.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 1 to zero.
 */
uint8_t FAN_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);


/**
 * @brief  Switch inhalator on.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 2 to one.
 */
uint8_t INH_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);


/**
 * @brief  Switch inhalator off.
 * @param  reg     Address of Port Register, such as &PORTB.
 * @param  pin     Pin designation in the interval 0 to 7.
 * @param  sw_flat Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                 If you do not want to use, set 0.      
 * @return Set bit 2 to zero.
 */
uint8_t INH_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat);

/**
 * @brief  Help function. Control fan. Usable if temperature is in required range and 
 *         humidity is higher than required value.
 * @param  fan_reg       Fan, address of Port Register, such as &PORTB.
 * @param  fan_pin       Fan, pin designation in the interval 0 to 7.
 * @param  current_hum   Measured humidity value.
 * @param  setpoint_hum  Required humidity value.
 * @param  hyst_hum      Hysteresis of humidity.
 * @param  sw_flat       Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                       If you do not want to use, set 0.      
 * @return Set bit 1 to zero if fan was not switched. Set bit 1 to one if fan was switched.
 */
uint8_t FAN_control_CT_HH(volatile uint8_t *fan_reg, uint8_t fan_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat);

/**
 * @brief  Help function. Control inhalator. Usable if heater is running.
 * @param  inha_reg      Inhalator, address of Port Register, such as &PORTB.
 * @param  inha_pin      Inhalator, pin designation in the interval 0 to 7.
 * @param  current_hum   Measured humidity value.
 * @param  setpoint_hum  Required humidity value.
 * @param  hyst_hum      Hysteresis of humidity.
 * @param  sw_flat       Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                       If you do not want to use, set 0.      
 * @return Set bit 2 to zero if inhalator was not switched. Set bit 2 to one if inhalator was switched.
 */
uint8_t INH_control_VHT(volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat);

/**
 * @brief  Help function. Control fan and inhalator. Temperature is in required range.
 * @param  fan_reg       Fan, address of Port Register, such as &PORTB.
 * @param  fan_pin       Fan, pin designation in the interval 0 to 7.
 * @param  inha_reg      Inhalator, address of Port Register, such as &PORTB.
 * @param  inha_pin      Inhalator, pin designation in the interval 0 to 7.
 * @param  current_hum   Measured humidity value.
 * @param  setpoint_hum  Required humidity value.
 * @param  hyst_hum      Hysteresis of humidity.
 * @param  sw_flat       Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                       If you do not want to use, set 0.      
 * @return Set bit 1 to zero if fan was not switched. Set bit 1 to one if fan was switched. 
 *         Set bit 2 to zero if inhalator was not switched. Set bit 2 to one if inhalator was switched.
 */
uint8_t INH_FAN_control_CT(volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat);

/**
 * @brief  Control heater, fan and inhalator
 * @param  heater_reg    Heater, address of Port Register, such as &PORTB.
 * @param  heater_pin    Heater, pin designation in the interval 0 to 7.
 * @param  fan_reg       Fan, address of Port Register, such as &PORTB.
 * @param  fan_pin       Fan, pin designation in the interval 0 to 7.
 * @param  inha_reg      Inhalator, address of Port Register, such as &PORTB.
 * @param  inha_pin      Inhalator, pin designation in the interval 0 to 7.
 * @param  current_temp  Measured temperature value.
 * @param  setpoint_temp Required temperature value.
 * @param  hyst_temp     Hysteresis of temperature.
 * @param  current_hum   Measured humidity value.
 * @param  setpoint_hum  Required humidity value.
 * @param  hyst_hum      Hysteresis of humidity.
 * @return None
 * @details Maximum value is required value plus hysteresis. Minimum value is required value
 *          minus hysteresis. Required value is typical value.
 *          Heater is switched on, if temperature is lower than minimum value or if temperature
 *          is lower than typical value and heater was switched on.
 *          Fan is switched on, if temperature is higher than maximum value or if temperature
 *          is higher than typical value and fan was switched on. Futhermore, when humidity
 *          is higher than maximum value or when it is higher than typical value and fan 
 *          was switched on. In this case, heater cannot be switched on.
 *          Inhalator is switched on, if humidity is lower than minimum value or if humidity
 *          is lower than typical value and inhalator was switched on. Fan cannot be switched on.
 *          Heater and inhalator can work simultaneously. Another combination are forbidden.
 */
void HEATER_FAN_control(volatile uint8_t *heater_reg, uint8_t heater_pin, volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_temp, uint8_t setpoint_temp, uint8_t hyst_temp, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum);
/** @} */

#endif