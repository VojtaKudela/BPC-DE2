/* 
 * PWM libary
 * (c) Vít Janoš 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

// -- Includes -------------------------------------------------------
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
    DDRD |= (1<<PD6); 
    TCCR0A |= (1 << WGM00) | (1 << WGM01) | (1 << COM0A1); // Fast PWM, non-inverted output on OC0A
    TCCR0B &= ~(1<<CS02); TCCR0B |= (1<<CS01) | (1<<CS00); // Start timer with prescaler 64
}

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

/*
 * Function: PWM_control
 * Purpose:  Automatically control duty
 * Input(s): current_value - measured value
 *           set_value     - required value
 *           step          - step increase or decrease value
 * Returns:  none
 */
void PWM_control(uint16_t current_value, uint16_t set_value, uint8_t step)
{
    static uint8_t duty = 0;

    // duty <= (255 - step) - protect overflow
    if ((current_value < set_value) & (duty <= (255 - step)))
    {
        duty += step;
    }
    // (duty >= step)       - protect underflow
    else if ((current_value > set_value) & (duty >= step))
    {
        duty -= step;
    }
    
    PWM_set_duty(duty);
}