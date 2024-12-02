"""
#############################################################
 # 
 # Application for monitoring and controling embedded 
 # system uses in greenhouse.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @mainpage Trorical plants
#
# @section intro_sec Introduction
#
# The source code runs an application for operating a greenhouse for growing tropical plants.
#
# @section first_sec Usage
#
# The application allows to monitor and control embedded system in greenhouse.
# It provide user-friendly GUI in Custom TKinter, which enables display current measured
# value as a number and also as a state of indicator. The application enables to display
# temperature, soil moisure, humidity and illumination.
#
# @section second_sec Connect
#
# For getting data is necessary to connect embedded device via UART. Press CONNECT for start 
# serial commincation. It show RUN button, if serial communication start properly. After pressing
# RUN, communication starts.
# 
# @section third_sec Graphical results
#
# Received data are storage in text file database.txt. They can be reprocessing. After click 
# to GRAPHICAL RESULTS buttom, window with graph will be showed. It allows to display a course 
# of the monitored quantities. It is possible to display data from last minute, last hour,
# last day, last week, last month, last year or all available data.
#
# @section fourth_sec Settings
#
# The application enables to set time on embedded device and set value and hysteresis which
# have to be regulated in greenhouse. Also regulated values are showed.  
#
# @author    Antonin Putala, Dept. of Radio Electronics, Brno University 
#            of Technology, Czechia
# @copyright (c) 2024 Antonin Putala, This work is licensed under 
#                the terms of the MIT license
##

##
# @file
# @defgroup  putala_top Application Tropical_plants
#
# @brief     The source code runs an application for operating a greenhouse for growing tropical plants.
#
# @details   The application allows to monitor and control embedded system in greenhouse.
#            It provide user-friendly GUI in Custom TKinter, which enables display current measured
#            value as a number and also as a state of indicator. The application enables to display
#            temperature, soil moisure, humidity and illumination.
#
#            For getting data is necessary to connect embedded device via UART. Press CONNECT for start 
#            serial commincation. It show RUN button, if serial communication start properly. After pressing
#            RUN, communication starts.
# 
#            Received data are storage in text file database.txt. They can be reprocessing. After click 
#            to GRAPHICAL RESULTS buttom, window with graph will be showed. It allows to display a course 
#            of the monitored quantities. It is possible to display data from last minute, last hour,
#            last day, last week, last month, last year or all available data.
#             
#            The application enables to set time on embedded device and set value and hysteresis which
#            have to be regulated in greenhouse. Also regulated values are showed.  
#
# @author    Antonin Putala, Dept. of Radio Electronics, Brno University 
#            of Technology, Czechia
# @copyright (c) 2024 Antonin Putala, This work is licensed under 
#                the terms of the MIT license
# @{

## Import application
from GUI_main import App

## Run application. Application runs, if program continues.
if __name__ == "__main__":  
    interface = App("COM3",9600)
    interface.mainloop()

##@}