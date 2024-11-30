"""
#############################################################
 # 
 # Library for displaying measured values.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win_fnc lib update_measure_value_func
 # @code import update_measure_value_func @endcode
 #
 # @brief It contains functions that overwrite the text field 
 #        with the value and set the correct indicator level 
 #        depending on the measured value.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

# Imports
import math as mt # To calculate the logarithm.

"""
# @brief   Changes the temperature value in the text field 
#          and changes the state of the indicator.
# @param   None
# @return  None
# @note    The data is taken from the main window 
#          directory self.measure_value['temp'].
"""
def update_temp(self):
    """
    Indicator level settings. The scale starts at 15 and is divided 
    into 47 divisions.
    """
    self.temp_progress.set((self.measure_value['temp']-15)/47)
    """
    Display of the measured value in a text field. 
    Whole numbers are displayed with the suffix .0.
    """
    temp = str(self.measure_value['temp'])
    if round(self.measure_value['temp'])==self.measure_value['temp']:
        temp += ".0"
    self.txt_temp.configure(text= temp + "°C")

"""
# @brief   Changes the humidity value in the text field 
#          and changes the state of the indicator.
# @param   None
# @return  None
# @note    The data is taken from the main window 
#          directory self.measure_value['hum'].
"""
def update_hum(self):
    """
    Indicator level settings. The scale starts at 0 and is divided 
    into 100 divisions.
    """
    self.hum_progress.set((self.measure_value['hum'])/100)
    """
    Display of the measured value in a text field. 
    Whole numbers are displayed with the suffix .0.
    """
    temp = str(self.measure_value['hum'])
    if round(self.measure_value['hum'])==self.measure_value['hum']:
        temp += ".0"
    self.txt_hum.configure(text= temp + "%")

"""
# @brief   Changes the soil moisure value in the text field 
#          and changes the state of the indicator.
# @param   None
# @return  None
# @note    The data is taken from the main window 
#          directory self.measure_value['soil'].
"""
def update_soil(self):
    self.soil_progress.set((self.measure_value['soil'])/100)
    """
    Indicator level settings. The scale starts at 0 and is divided 
    into 100 divisions.
    """
    temp = str(self.measure_value['soil'])
    """
    Display of the measured value in a text field. 
    Whole numbers are displayed with the suffix .0.
    """
    if round(self.measure_value['soil'])==self.measure_value['soil']:
        temp += ".0"
    self.txt_soil.configure(text= temp + "%" )

"""
# @brief   Changes the illumination value in the text field 
#          and changes the state of the indicator.
# @param   None
# @return  None
# @note    The data is taken from the main window 
#          directory self.measure_value['ilu'].
"""
def update_ilu(self):
    """
    Indicator level settings. The scale starts at 1 and ends at 1000. 
    It is logarithmic.
    """
    self.ilu_progress.set((mt.log10(self.measure_value['ilu']))/3)
    """Display of the measured value in a text field."""
    temp = str(self.measure_value['ilu'])
    self.txt_ilu.configure(text= temp + " lx" )

"""@}"""