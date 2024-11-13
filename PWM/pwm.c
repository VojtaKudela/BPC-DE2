/* 
 * PWM libary
 * (c) Vít Janoš 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

// -- Includes -------------------------------------------------------
#include <gpio.h>
#include <pwm.h>

// -- Function definitions -------------------------------------------
/*
 * Function: PWM_enable
 * Purpose:  Enable PWM
 * Input(s): none
 * Returns:  none
 */
void PWM_enable()
{
    GPIO_mode_output(&DDRD, PD6);
    TCCR0A |= (1 << WGM00) | (1 << WGM01) | (1 << COM0A1); // Fast PWM, non-inverted output on OC0A
    TCCR0B &= ~(1<<CS02); TCCR0B |= (1<<CS01) | (1<<CS00); // Start timer with prescaler 64
}

// -- Function definitions -------------------------------------------
/*
 * Function: PWM_set_duty
 * Purpose:  Sets duty cycle
 * Input(s): duty - 0 - 255 when 0 = 0% and 255 = 100%
 * Returns:  none
 */

void PWM_set_duty(volatile uint8_t duty)
{
    OCR0A = duty;
}