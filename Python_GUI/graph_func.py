"""
#############################################################
 # 
 # The library contains functions for setting graph axes.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win_fnc lib graph_func
 # @code import graph_func @endcode
 #
 # @brief The library contains functions for setting correct 
 #        axis labels, as well as functions for determining days 
 #        in a month, days in a year, and days in a specific month.
 #
 # @note  All functions affect the Graphical results window.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

"""
# @brief   Depending on the timeline settings, 
#          it will select the appropriate 
#          timeline description.
# @param   None
# @return  None
# @note    The setting in the drop-down menu 
#          is decisive.
"""
def set_xlabel(self):
    match (self.time_scale.get()):
        case 'Last minute':
            self.ax.set_xlabel('Time [sec]')
        case 'Last hour':
            self.ax.set_xlabel('Time [min]')
        case 'Last day':
            self.ax.set_xlabel('Time [hour]')
        case 'Last week':
            self.ax.set_xlabel('Time [day]')
        case 'Last month':
            self.ax.set_xlabel('Time [day]')
        case 'Last year':
            self.ax.set_xlabel('Time [month]')
        case _:
            self.ax.set_xlabel('Time [year]')

"""
# @brief   Depending on the selected quantity, 
#          it selects an appropriate vertical 
#          axis description.
# @param   None
# @return  None
# @note    The setting in the radio button menu 
#          is decisive.
"""
def set_ylabel(self):
    match (self.radio_var.get()):
        case 1:
            self.ax.set_ylabel('Temperature [°C]')
        case 2:
            self.ax.set_ylabel('Humidity [%]')
        case 3:
            self.ax.set_ylabel('Soil moisure [%]')
        case _:
            self.ax.set_ylabel('Illumination [lx]')

"""
# @brief   Based on the month and year, 
#          it determines how many days a month has.
# @param   month (str) for determining the number of days.
# @param   year  (str) to distinguish leap years.
# @return  Number of days in a given month.
# @note    It also takes leap years into account.
"""
def n_of_days(month,year):
    # April, June, September and November have 30 days
    if ((month == "4") | (month == "6") | (month == "9") | (month == "11")):
        return 30
    # February 28 or 29 days
    elif ((month == "2")):
        if ((int(year) % 4) == 0):
            # leap year
            return 29
        else:
            # normal year
            return 28
    # Other months have 31 days
    else:
        return 31

"""
# @brief   Specifies the number of days in a year.
# @param   year  (str) to determine the number of days.
# @return  Number of days in a given year.
# @warning It considers a leap year every four years. 
#          Other rules are not respected.
"""    
def n_of_days_year(year):
    if (int(year) % 4 == 0):
        return 365
    else:
        return 366
    
"""
# @brief   Specifies the number of days before a given month.
# @param   month (str) for determining the number of days.
# @param   year  (str) to distinguish leap years.
# @return  How many days pass before the month begins.
# @note    It also takes leap years into account.
"""
def n_of_days_cum(month,year):
    days = 0
    for j in range(1,int(month),1):
        days += n_of_days(str(j),year)
    return days

"""@}"""
        
