/* 
 * Preper_Data libary
 * (c) Antonin Putala 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 * Tested by Online C Compiler https://www.online-cpp.com/online_c_compiler
 */

// -- Includes -------------------------------------------------------
#include <preper_data.h>

// -- Function definitions -------------------------------------------
/*
 * Function: PD_round
 * Purpose:  Rounded number with decimal and integer part.
 * Input(s): int_part - integer part of number
 *           dec_part - decimal part of number
 * Returns:  rounded value
 */
uint8_t PD_round(uint8_t int_part, uint8_t dec_part)
{
    if (dec_part > 4)
    {
        return int_part+1;
    }
    else
    {
        return int_part;
    }
}

/*
 * Function: PD_uart
 * Purpose:  Prepered illumination and soil moisure for transmission.
 * Input(s): value - 10-bit output ADC
 *           mask  - Forbidden value
 * Returns:  8-bit data prepered for UART
 */
uint8_t PD_uart(uint16_t value, uint8_t mask)
{
    // Local variables
    uint8_t ret_value;

    // Preper transmit value
    ret_value = value>>2;

    // Check mask conditions for lux and soil
    if (ret_value == mask)
    {
        return ret_value += 1;
    }  
    else
    {
        return ret_value;
    }
}

/*
 * Function: PD_ilu
 * Purpose:  Calculate the illumination value.
 * Input(s): value - 16-bit, output of ADC
 * Returns:  16-bit, sensible value of illumination
 */
uint16_t PD_ilu(uint16_t value)
{
    return (value-16)+10;
}

/*
 * Function: PD_soil
 * Purpose:  Calculate the soil moisure value.
 * Input(s): value - 16-bit, output of ADC
 * Returns:  16-bit, sensible value of soil moisure
 */
uint8_t PD_soil(uint16_t value)
{
    uint8_t ret_value;
    ret_value = value>>2;
    return 100-(ret_value-180)*2;
}