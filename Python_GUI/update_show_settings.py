"""
#############################################################
 # 
 # Function for displaying the set regulation values.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win_fnc lib update_show_settings
 # @code import update_show_settings @endcode
 #
 # @brief The function allows you to overwrite text fields 
 #        that display the set values of individual quantities 
 #        and their hysteresis.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

"""
# @brief   Changes the displayed values of 
#          regulation variables and hysteresis.
# @param   self Main window.
# @return  None
"""
def update_show_settings(self):
    """Changes illumination value."""
    temp = str(self.setting['ilu_val']) + " lx"
    self.txt_set_ilu_value.configure(text=temp)

    """Changes humidity value."""
    temp = str(self.setting['hum_val']) + " % ± " + str(self.setting['hum_hys']) + " %"
    self.txt_set_hum_value.configure(text=temp)

    """Changes soil moisure value."""
    temp = str(self.setting['soil_val']) + " % ± " + str(self.setting['soil_hys']) + " %"
    self.txt_set_soil_value.configure(text=temp)

    """Changes temperature value."""
    temp = str(self.setting['temp_val']) + "°C ± " + str(self.setting['temp_hys']) + "°C"
    self.txt_set_temp_value.configure(text=temp)

"""@}"""