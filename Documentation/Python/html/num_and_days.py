"""
#############################################################
 # 
 # A library that contains functions for converting 
 # the day of the week to a number and vita versa.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_day_func Day functions
# @code import num_and_days @endcode
#
# @brief This function allows you to convert the name of 
#        the month to its order.
#
# @note The function is used in the GUI to set the time 
#       to get the numeric value from the month drop-down menu.
#
# @author Antonin Putala, Dept. of Radio Electronics, Brno University 
#         of Technology, Czechia
# @copyright (c) 2024 Antonin Putala, This work is licensed under 
#                the terms of the MIT license
#@{

def day2num(day):
    """!
    @brief  The function converts the name of the day of 
            the week to a numeric value. 
    @param  day The first two letters of the English name 
            of the day of the week
    @return Order of the day of the week.
    @retval Su - 0, Mo - 1, Tu - 2, We - 3, Th - 4, Fr - 5, Sa - 6.
    """
    match (day):
        case 'Mo':
            return 1
        case 'Tu':
            return 2
        case 'We':
            return 3
        case 'Th':
            return 4
        case 'Fr':
            return 5
        case 'Sa':
            return 6
        case _:
            return 0
        
def num2day(num):
    """!
    @brief  This function allows you to convert its order of the day
            of the week to the first two letter one's name.
    @param  num Day of the week number.
    @return The first letter of the name of th day of the week.
    @retval 0 - So, 1 - Mo, 2 - Tu, 3 - We, 4 - Th, 5 - Fr, 6 - Sa.
    """    
    match (num):
        case 1:
            return 'Mo'
        case 2:
            return 'Tu'
        case 3:
            return 'We'
        case 4:
            return 'Th'
        case 5:
            return 'Fr'
        case 6:
            return 'Sa'
        case _:
            return 'Su'
            
##@}