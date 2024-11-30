"""
#############################################################
 # 
 # The library contains functions for creating and updating 
 # main window data.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win_fnc lib data_func
 # @code import data_func @endcode
 #
 # @brief The library contains functions for creating 
 #        the main window data and for filling the sent data
 #        package with controls.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

"""
# @brief   Creates individual data stores for the main window. 
#          It fills them with default data.
# @param   None
# @return  None
# @details The following directories are created:
#            # settings       -  It contains set values of controlled 
#                                variables and hysteresis.
#            # system_settings - It contains the allowed ranges of 
#                                values and hysteresis.
#            # measure_value   - The received measured values of 
#                                the quantities will be stored here.
#          The following lists are created:
#            # time_packet     - This is where the time setting data 
#                                is stored before it is sent. The first 
#                                byte is always the ASCII code 'T' 
#                                for recognition.
#            # reg_packet      - This is where the regulation setting data 
#                                is stored before it is sent. The first 
#                                byte is always the ASCII code 'R' 
#                                for recognition.
#          It also creates a repository for connection phase information.
#          Phase: 0 - no connection.
#          Phase: 1 - preperation to start.
#          Phase: 2 - communication is running.
"""
def default_data(self):
    self.setting = {'temp_val':25,'temp_hys':2,'hum_val':50,'hum_hys':5,
                    'soil_val':50,'soil_hys':5,'ilu_val':100}
    self.system_setting = {'ilu_min':20,'ilu_max':500,'temp_val_min':15,
                            'temp_val_max':50,'temp_hys_min':1,'temp_hys_max':10,
                            'hum_val_min':20,'hum_val_max':90,'hum_hys_min':5,'hum_hys_max':30,
                            'soil_val_min':5,'soil_val_max':90,'soil_hys_min':5,'soil_hys_max':30}
    self.measure_value = {'temp':20,'hum':65.7,'soil':54,'ilu':200}
    self.time_packet = [0x54,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    self.reg_packet = [0x52,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    self.phase = 0

"""
# @brief   It fills the package with the control values 
#          with the current values.
# @param   None
# @return  None
# @details Data is taken from the self.settings dictionary.
"""
def full_reg_data(self):
    self.reg_packet[1] = self.setting['temp_val']
    self.reg_packet[2] = self.setting['temp_hys']
    self.reg_packet[3] = self.setting['hum_val']
    self.reg_packet[4] = self.setting['hum_hys']
    self.reg_packet[5] = self.setting['soil_val']
    self.reg_packet[6] = self.setting['soil_hys']
    self.reg_packet[7] = self.setting['ilu_val']//100
    self.reg_packet[8] = self.setting['ilu_val']%100

"""@}""" 