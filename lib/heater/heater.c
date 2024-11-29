/***********************************************************
 * 
 * GPIO library for AVR-GCC.
 * (c) 2024 Vojtech Kudela, Antonin Putala
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 * Tested using Simulide.
 ***********************************************************/

/* Includes ------------------------------------------------*/
#include <heater.h>

/* Function definitions -----------------------------------*/
/***********************************************************
 * Function: HEATER_init()
 * Purpose:  Initialize heater pin, switch heater off.
 * Input(s): reg - Address of Port Register, such as &PORTB.
 *           pin - Pin designation in the interval 0 to 7.
 * Returns:  none
 ***********************************************************/
void HEATER_init(volatile uint8_t *reg, uint8_t pin)
{
    // Set pin as output
    *reg |= (1<<pin);
    // Start value
    *(reg+1) &= ~(1<<pin);
}

/***********************************************************
 * Function: FAN_init()
 * Purpose:  Initialize fan pin, switch fan off.
 * Input(s): reg - Address of Port Register, such as &PORTB.
 *           pin - Pin designation in the interval 0 to 7.
 * Returns:  none
 ***********************************************************/
void FAN_init(volatile uint8_t *reg, uint8_t pin)
{
    // Set pin as output
    *reg |= (1<<pin);
    // Start value
    *(reg+1) &= ~(1<<pin);
}

/***********************************************************
 * Function: INH_init()
 * Purpose:  Initialize inhalator pin, switch inhalator off.
 * Input(s): reg - Address of Port Register, such as &PORTB.
 *           pin - Pin designation in the interval 0 to 7.
 * Returns:  none
 ***********************************************************/
void INH_init(volatile uint8_t *reg, uint8_t pin)
{
    // Set pin as output
    *reg |= (1<<pin);
    // Start value
    *(reg+1) &= ~(1<<pin);
}

/***********************************************************
 * Function: HEATER_on()
 * Purpose:  Switch heater on.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 0 to one.
 ***********************************************************/
uint8_t HEATER_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat |= (1<<HEAT_BIT);
    *reg |= (1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: HEATER_off()
 * Purpose:  Switch heater off.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 0 to zero.
 ***********************************************************/
uint8_t HEATER_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat &= ~(1<<HEAT_BIT);
    *reg &= ~(1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: FAN_on()
 * Purpose:  Switch fan on.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 1 to one.
 ***********************************************************/
uint8_t FAN_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat |= (1<<FAN_BIT);
    *reg |= (1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: FAN_off()
 * Purpose:  Switch fan off.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 1 to zero.
 ***********************************************************/
uint8_t FAN_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat &= ~(1<<FAN_BIT);
    *reg &= ~(1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: INH_on()
 * Purpose:  Switch inhalator on.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 2 to one.
 ***********************************************************/
uint8_t INH_on(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat |= (1<<INH_BIT);
    *reg |= (1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: INH_off()
 * Purpose:  Switch inhalator off.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 *           sw_flat - Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs;
 *                     If you do not want to use, set 0.
 * Returns:  Set bit 2 to zero.
 ***********************************************************/
uint8_t INH_off(volatile uint8_t *reg, uint8_t pin, uint8_t sw_flat)
{
    sw_flat &= ~(1<<INH_BIT);
    *reg &= ~(1<<pin);
    return sw_flat;
}

/***********************************************************
 * Function: FAN_control_CT_HH()
 * Purpose:  Help function. Control fan. Usable if temperature is in required 
 *           range and humidity is higher than required value.
 * Input(s): fan_reg       - Fan, address of Port Register, such as &PORTB.
 *           fan_pin       - Fan, pin designation in the interval 0 to 7.
 *           current_hum   - Measured humidity value.
 *           setpoint_hum  - Required humidity value.
 *           hyst_hum      - Hysteresis of humidity.
 *           sw_flat       - Flat of running devices: bit 2 inhalator runs, 
 *                           bit 1 fan runs, bit 0 heater runs;
 *                           If you do not want to use, set 0.
 * Returns:  Set bit 1 to zero if fan was not switched. Set bit 1 to one if fan was switched.
 ***********************************************************/
uint8_t FAN_control_CT_HH(volatile uint8_t *fan_reg, uint8_t fan_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat)
{
    // Humidity is higher than require maximum, fan was stopped.
    if (((sw_flat & (1 << FAN_BIT)) == 0) & (current_hum > (setpoint_hum + hyst_hum)))
    {
        sw_flat = FAN_on(fan_reg, fan_pin, sw_flat);
    }
    // Humidity is higher than typycal value, fan runs.
    else if (((sw_flat & (1 << FAN_BIT)) != 0) & (current_hum > setpoint_hum))
    {
        sw_flat = FAN_on(fan_reg, fan_pin, sw_flat);
    }
    // Humidity is in required range.
    else
    {
        sw_flat = FAN_off(fan_reg, fan_pin, sw_flat);
    }
    return sw_flat;
}

/***********************************************************
 * Function: INH_control_VHT()
 * Purpose:  Help function. Control inhalator. Usable if heater is running.
 * Input(s): inha_reg      - Inhalator, address of Port Register, such as &PORTB.
 *           inha_pin      - Inhalator, pin designation in the interval 0 to 7.
 *           current_hum   - Measured humidity value.
 *           setpoint_hum  - Required humidity value.
 *           hyst_hum      - Hysteresis of humidity.
 *           sw_flat       - Flat of running devices: bit 2 inhalator runs, 
 *                           bit 1 fan runs, bit 0 heater runs;
 *                           If you do not want to use, set 0.
 * Returns:  Set bit 2 to zero if fan was not switched. Set bit 2 to one if fan was switched.
 ***********************************************************/
uint8_t INH_control_VHT(volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat)
{
    // Inhalator was stopped, hum is lower than required minimum.
    if (((sw_flat & (1 << INH_BIT)) == 0) & (current_hum < (setpoint_hum - hyst_hum)))
    {
        sw_flat = INH_on(inha_reg, inha_pin, sw_flat);
    }
    // Inhalator runs, hum is lower typical value.
    else if (((sw_flat & (1 << INH_BIT)) != 0) & (current_hum < setpoint_hum))
    {
        sw_flat = INH_on(inha_reg, inha_pin, sw_flat);
    }
    // Humidity is in required range.
    else
    {
        sw_flat = INH_off(inha_reg, inha_pin, sw_flat);
    }
    return sw_flat;
}

/***********************************************************
 * Function: INH_FAN_control_CT()
 * Purpose:  Help function. Control fan and inhalator. Temperature is in required range.
 * Input(s): fan_reg       - Fan, address of Port Register, such as &PORTB.
 *           fan_pin       - Fan, pin designation in the interval 0 to 7.
 *           inha_reg      - Inhalator, address of Port Register, such as &PORTB.
 *           inha_pin      - Inhalator, pin designation in the interval 0 to 7.
 *           current_hum   - Measured humidity value.
 *           setpoint_hum  - Required humidity value.
 *           hyst_hum      - Hysteresis of humidity.
 *           sw_flat       - Flat of running devices: bit 2 inhalator runs, 
 *                           bit 1 fan runs, bit 0 heater runs;
 *                           If you do not want to use, set 0.
 * Returns:  Set bit 1 to zero if fan was not switched. Set bit 1 to one if fan was switched. 
 *           Set bit 2 to zero if inhalator was not switched. Set bit 2 to one if inhalator was switched.
 ***********************************************************/
uint8_t INH_FAN_control_CT(volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum, uint8_t sw_flat)
{
    // Inhalator was stopped, hum is lower than required minimum.
    if (((sw_flat & (1 << INH_BIT)) == 0) & (current_hum < (setpoint_hum - hyst_hum)))
    {   
        sw_flat = INH_on(inha_reg, inha_pin, sw_flat);
        sw_flat = FAN_off(fan_reg, fan_pin, sw_flat);
    }
    // Inhalator runs, hum is lower typical value.
    else if (((sw_flat & (1 << INH_BIT)) != 0) & (current_hum < setpoint_hum))
    {
        sw_flat = INH_on(inha_reg, inha_pin, sw_flat);
        sw_flat = FAN_off(fan_reg, fan_pin, sw_flat);
    }
    // Humidity is higher than required minimum.
    else
    {
        sw_flat = INH_off(inha_reg, inha_pin, sw_flat);
        sw_flat = FAN_control_CT_HH(fan_reg, fan_pin, current_hum, setpoint_hum, hyst_hum, sw_flat);
    }
    return sw_flat;
}

/***********************************************************
 * Function: HEATER_FAN_control()
 * Purpose:  Control heater, fan and inhalator.
 * Input(s): heater_reg    - Heater, address of Port Register, such as &PORTB.
 *           heater_pin    - Heater, pin designation in the interval 0 to 7.
 *           fan_reg       - Fan, address of Port Register, such as &PORTB.
 *           fan_pin       - Fan, pin designation in the interval 0 to 7.
 *           inha_reg      - Inhalator, address of Port Register, such as &PORTB.
 *           inha_pin      - Inhalator, pin designation in the interval 0 to 7.
 *           current_temp  - Measured temperature value.
 *           setpoint_temp - Required temperature value.
 *           hyst_temp     - Hysteresis of temperature.
 *           current_hum   - Measured humidity value.
 *           setpoint_hum  - Required humidity value.
 *           hyst_hum      - Hysteresis of humidity.
 * Returns:  None
 ***********************************************************/
void HEATER_FAN_control(volatile uint8_t *heater_reg, uint8_t heater_pin, volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, uint8_t current_temp, uint8_t setpoint_temp, uint8_t hyst_temp, uint8_t current_hum, uint8_t setpoint_hum, uint8_t hyst_hum)
{   
    // Flat of running devices: bit 2 inhalator runs, bit 1 fan runs, bit 0 heater runs.
    static uint8_t sw_flat = 0;  

    // Heater was stopped.
    if ((sw_flat & (1 << HEAT_BIT)) == 0)
    {
        // Lower than required minimum of temp.
        if (current_temp < (setpoint_temp - hyst_temp))
        {
            sw_flat = HEATER_on(heater_reg, heater_pin, sw_flat);
            sw_flat = FAN_off(fan_reg, fan_pin, sw_flat);
            sw_flat = INH_control_VHT(inha_reg, inha_pin, current_hum, setpoint_hum, hyst_hum, sw_flat);
        }
        // Higher than required minimum of temperature.
        else
        {
        // Fan was stopped, temperature is higher than required maximum.
            if (((sw_flat & (1 << FAN_BIT)) == 0) & (current_temp > (setpoint_temp + hyst_temp)))
            {
                sw_flat = HEATER_off(heater_reg, heater_pin, sw_flat);
                sw_flat = FAN_on(fan_reg, fan_pin, sw_flat); 
                sw_flat = INH_off(inha_reg, inha_pin, sw_flat);
            }
        // Fan runs, temperature is higher than typical value.
            else if (((sw_flat & (1 << FAN_BIT)) != 0) & (current_temp > setpoint_temp))
            {
                sw_flat = HEATER_off(heater_reg, heater_pin, sw_flat);
                sw_flat = FAN_on(fan_reg, fan_pin, sw_flat);
                sw_flat = INH_off(inha_reg, inha_pin, sw_flat);
            }
        // Temperature is in allowed range.
            else
            {
                sw_flat = HEATER_off(heater_reg, heater_pin, sw_flat);
                sw_flat = INH_FAN_control_CT(fan_reg, fan_pin, inha_reg, inha_pin, current_hum, setpoint_hum, hyst_hum, sw_flat);
            }
        }
    }
    // Heater runs.
    else
    {
        // Temperature is lower than typical value.
        if (current_temp < setpoint_temp)
        {
            sw_flat = HEATER_on(heater_reg, heater_pin, sw_flat);
            sw_flat = FAN_off(fan_reg, fan_pin, sw_flat);   
            sw_flat = INH_control_VHT(inha_reg, inha_pin, current_hum, setpoint_hum, hyst_hum, sw_flat);
        }
        // Temperature is higher than required maximum, if heater runs, fans cannot work.
        else if (current_temp > (setpoint_temp + hyst_temp))
        {
            sw_flat = HEATER_off(heater_reg, heater_pin, sw_flat);
            sw_flat = FAN_on(fan_reg, fan_pin, sw_flat);
            sw_flat = INH_off(inha_reg, inha_pin, sw_flat);
        }
        // Temperature is in required range.
        else
        {
            sw_flat = HEATER_off(heater_reg, heater_pin, sw_flat);
            sw_flat = INH_FAN_control_CT(fan_reg, fan_pin, inha_reg, inha_pin, current_hum, setpoint_hum, hyst_hum, sw_flat);
        }
    }
}