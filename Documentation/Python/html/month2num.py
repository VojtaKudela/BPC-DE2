"""
#############################################################
 # 
 # Function to convert month name to number.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_month_func Month function
# @code import month2num @endcode
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
# @{


def month2num(month):
    """!
    @brief  This function allows you to convert the name of 
            the month to its order. 
    @param  month English name of the month.
    @return Order of the month.
    """
    match(month):
        case "January":
            return 1
        case "February":
            return 2
        case "March":
            return 3
        case "April":
            return 4
        case "May":
            return 5
        case "June":
            return 6
        case "July":
            return 7
        case "August":
            return 8
        case "September":
            return 9
        case "October":
            return 10
        case "November":
            return 11
        case "December":
            return 12
        case _:
            return 13
        
##@}