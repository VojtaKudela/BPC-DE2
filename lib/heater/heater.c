/* 
 * GPIO library for AVR-GCC.
 * (c) 2024 Vojtěch Kudela
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

// -- Includes -------------------------------------------------------
#include <heater.h>

// inicializace pinu jako výstupní pro ovládání topení
void HEATER_init(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}

// inicializace pinu jako výstupu pro ovládání větráčku
void FAN_init(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}

// inicializace pinu jako výstupu pro ovládání inhalatoru
void INH_init(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}


// Funkce pro zapnuti a vypnuti topeni
// zapnuti topeni na vysokou uroven
void HEATER_on(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}
;
// vypnutí topení na nízkou úroveň
void HEATER_off(volatile uint8_t *reg, uint8_t pin)
{
    *reg &= ~(1<<pin);
}

// Funkce pro zapnutí a vypnutí větráčku
// zapnutí větráčku na vysokou úroveň
void FAN_on(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}

// vypnutí větráčku na nízkou úroveň
void FAN_off(volatile uint8_t *reg, uint8_t pin)
{
    *reg &= ~(1<<pin);
}

// Function for switching on and switching off of inhalator
// Start inhalator
void INH_on(volatile uint8_t *reg, uint8_t pin)
{
    *reg |= (1<<pin);
}

// Stop inhalator
void INH_off(volatile uint8_t *reg, uint8_t pin)
{
    *reg &= ~(1<<pin);
}

// ovládání topení a větráčku na základě aktuální hodnoty, nastavení teploty a hystereze
// pokud je aktuální hodnota nižší, tak se topení zapne a větráček se vypne
// pokud je aktuální hodnota vyšší, tak se topení vypne a větráček se zapne
void HEATER_FAN_control(volatile uint8_t *heater_reg, uint8_t heater_pin, volatile uint8_t *fan_reg, uint8_t fan_pin, volatile uint8_t *inha_reg, uint8_t inha_pin, int8_t current_temp, int8_t setpoint_temp, int8_t hyst_temp, int8_t current_hum, int8_t setpoint_hum, int8_t hyst_hum)
{   

    if(current_temp < (setpoint_temp - hyst_temp))
    {
        HEATER_on(heater_reg, heater_pin);
        FAN_off(fan_reg, fan_pin);
        if (current_hum < (setpoint_hum - hyst_hum))
        {
            INH_on(inha_reg, inha_pin);
        }
        else
        {
            INH_off(inha_reg, inha_pin);
        }
    }

    else if(current_temp > (setpoint_temp + hyst_temp))
    {
        HEATER_off(heater_reg, heater_pin);
        FAN_on(fan_reg, fan_pin);
        INH_off(inha_reg, inha_pin);
    }
    else
    {
        HEATER_off(heater_reg, heater_pin);

        if (current_hum < (setpoint_hum - hyst_hum))
        {
            INH_on(inha_reg, inha_pin);
            FAN_off(fan_reg, fan_pin);  
        }
        else if ((current_hum > (setpoint_hum + hyst_hum)))
        {
            INH_off(inha_reg, inha_pin);
            FAN_on(fan_reg, fan_pin);  
        }
        else
        {
            INH_off(inha_reg, inha_pin);
            FAN_off(fan_reg, fan_pin); 
        }
             
    }
}
// k nastavení používá statické proměnné heater_state a fan_state
