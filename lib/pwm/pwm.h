#ifndef pwm_H
# define pwm_H
/* 
 * PWM libary
 * (c) Vít Janoš 2024
 *
 * Developed using PlatformIO and AVR 8-bit Toolchain 3.6.2.
 * Tested on Arduino Uno board and ATmega328P, 16 MHz.
 */

/**
 * @file 
 * @defgroup PWM libary <pwm.h>
 * @code #include <pwm.h> @endcode
 *
 * @brief PWM library for AVR-GCC.
 *
 * The library contains functions for controlling AVRs' PWM.
 *
 * @note Hope it works
 * @copyright (c) Vít Janoš 2024
 * @
 */
/* Includes -----------------------------------------------*/
#include <avr/io.h>

/* Function prototypes ------------------------------------*/
/**
 * @brief  Enables non-inverted PWM on timer 0
 * @return none
 */
void PWM_enable();

/**
 * @brief  Configures the duty cycle
 * @param  duty Sets the required duty cycle wher 0 is 0% and 255 is 100%
 * @return none
 */
void PWM_set_duty(volatile uint8_t duty);

/**
 * @brief  Automatically control duty cycle
 * @param  current_value Measured value
 * @param  set_value     Required value
 * @param  step          Step increase or decrease value
 * @return none
 */
void PWM_control(uint16_t current_value, uint16_t set_value, uint8_t step);

#endif
