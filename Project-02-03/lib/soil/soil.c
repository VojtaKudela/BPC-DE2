/* 
 * GPIO library for AVR-GCC.
 * (c) 2024 Vojtech Kudela
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz. 
 * Tested using Simulide.
 */

/* Includes ------------------------------------------------*/
#include <soil.h>

/***********************************************************
 * Function: SOIL_init()
 * Purpose:  Initialize valve pin, turn valve off.
 * Input(s): reg - Address of Port Register, such as &PORTB.
 *           pin - Pin designation in the interval 0 to 7.
 * Returns:  none
 ***********************************************************/
void SOIL_init(volatile uint8_t *reg, uint8_t pin)
{
    // set pin to output
    *reg |= (1<<pin);
    // set low level on valve pin
    *(reg-1) &= ~(1<<pin);
}


/***********************************************************
 * Function: SOIL_on()
 * Purpose:  Turn valve on.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 * Returns:  Set bit 0 to one.
 ***********************************************************/
uint8_t SOIL_on(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
    return 1;
}

/***********************************************************
 * Function: SOIL_off()
 * Purpose:  Turn valve off.
 * Input(s): reg     - Address of Port Register, such as &PORTB.
 *           pin     - Pin designation in the interval 0 to 7.
 * Returns:  Set bit 0 to zero.
 ***********************************************************/
uint8_t SOIL_off(volatile uint8_t *reg, uint8_t pin)
{
    *reg &= ~(1<<pin);
    return 0;
}

/***********************************************************
 * Function: SOIL_control()
 * Purpose:  Control valve.
 * Input(s): soil_reg      - Valve, address of Port Register, such as &PORTB.
 *           soil_pin      - Valve, pin designation in the interval 0 to 7.
 *           current_soil  - Measured soil moisure value.
 *           setpoint_soil - Required soil moisure value.
 *           hyst_soil     - Hysteresis of soil moisure.
 * Returns:  None
 ***********************************************************/
void SOIL_control(volatile uint8_t *soil_reg, uint8_t soil_pin, uint8_t current_soil, uint8_t setpoint_soil, uint8_t hyst_soil)
{
    static uint8_t soil_sw = 0; // 1 - if ventil was open, 0 - if ventil was close

    if ((soil_sw == 0) & (current_soil < (setpoint_soil - hyst_soil)))
    {
        soil_sw = SOIL_on(soil_reg, soil_pin);
    }
    else if((soil_sw == 1) & (current_soil < setpoint_soil))
    {
        soil_sw = SOIL_on(soil_reg, soil_pin);
    }
    else
    {
        soil_sw = SOIL_off(soil_reg ,soil_pin);
    }
}