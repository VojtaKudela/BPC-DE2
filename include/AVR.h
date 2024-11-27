#ifndef AVR_H
# define AVR_H

#define startconversion() ADCSRA |= (1 << ADSC);

#define setupADC() \
    (ADCSRA |= (1 << ADPS2) | (1 << ADPS1)); \
    (ADMUX |= (1 << REFS0) | (1 << MUX0) | (1 << MUX2)); \
    (ADCSRA |= (1 << ADEN) | (1 << ADIE));

#define switchport() ADMUX ^= (1 << MUX0);


#endif




/*
This section is to be added at the start of the program to load AVR.h and define variables.

#include "AVR.h"

volatile uint16_t data = 0;
volatile uint16_t data_0 = 0;
volatile uint16_t data_1 = 0;
volatile uint8_t reset = 0;
volatile uint8_t counter = 0;

*/

/*
This section is to be added to main function at the start to setup timer and ADC and enable interrupts.

  TIM2_ovf_16ms(); 
  TIM2_ovf_enable();

  setupADC();

  sei();

*/

/*
This section is to be added after main function to setup interupts for both timer and ADC.

ISR(TIMER2_OVF_vect)
{
    counter++;

    if (counter >= 6) 
    {
        counter = 0;
        reset = 1;
        switchport();
        startconversion();
    }
}

ISR(ADC_vect)
{
  data = ADC;  // Save the ADC value
}


*/

/*
This section is to be added to main function to an infinite loop to handle spliting the data from 2 ports and save them into a separate int.

    if (reset == 1)
    {
        if (ADMUX & (1 << MUX0)) {
        data_0 = data;
        } else {
        data_1 = data;
        }
    }
  }

*/