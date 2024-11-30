"""
#############################################################
 # 
 # Class for creating a whole application Tropical plants.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win class GUI_main
 # @code import GUI_main @endcode
 #
 # @brief The class provides window creation and serial 
 #        communication.
 # 
 # @note    It needs programs to function: # createGUImain,
 #                                         # createGUIset,
 #                                         # createGUIshow,
 #                                         # data_file     
 #                                         # date_func  
 #                                         # database  
 #                                         # graph_func
 #                                         # graphGUI  
 #                                         # GUIcreate  
 #                                         # hum_GUI  
 #                                         # ilu_GUI
 #                                         # month2num
 #                                         # num_and_days  
 #                                         # raw_data 
 #                                         # soil_GUI  
 #                                         # temp_GUI
 #                                         # time_GUI
 #                                         # update_show_settings
 #                                         # update_measure_value_func       
 #      
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

# Imports
import customtkinter as ckt             # Custom Tkinter is used to create GUI.

# Library for serial communication
import time                             # Setting how often received data is checked.
import serial                           # The library contains functions for handling the serial port.
import threading                        # The library allows you to have a window open and read data 
                                        # from the serial port at the same time.

# Function which create GUI
from GUI_create import createGUI        # Creates the main window.
from ilu_GUI import ilu_GUI             # Creates a window for illumination settings.
from soil_GUI import soil_GUI           # Creates a window for soil moisure settings.
from hum_GUI import hum_GUI             # Creates a window for humidity settings.
from temp_GUI import temp_GUI           # Creates a window for temperature settings.
from time_GUI import time_GUI           # Creates a window for time settings.
from graph_GUI import graph_GUI         # Creates a window for graphical results showing.

# Another fuction
from update_measure_value_func import * # Update indicators and texts.
from data_func import *                 # Functions for creating main window 
                                        # directories and preparing set cregulation data for sending.          
from raw_data import raw_data           # Receives data from serial port.
from data_file import data_file         # It processes data from the serial port.
from update_show_settings import *      # Displays the set regulation values.

class App(ckt.CTk):
    """
# @brief   Launches a window.
# @param   nserial    Selected serial port.
# @param   nbaud_rate Selected baud rate of serial communication.
# @return  None
# @details Creates individual GUI widgets. Creates directories 
#          with default data. Saves information about the serial port
#          and baud rate. Creates a directory for serial communication. 
#          Creates a data space for storing received data and a database.
    """
    def __init__(self, nserial_port = "COM3", nbaud_rate=9600):
        super().__init__()
        # Create GUI widgets.
        createGUI(self)
        # Create dictionaries with default data.
        self.default_data()
        # Save information about serial port and baud rate.
        self.serial_port = nserial_port
        self.baud_rate = nbaud_rate
        # Flat of running communication.
        self.running = True
        # Reference to a serial communication object.
        self.serial_connection = None
        # Create a repository of received data and a database.
        raw = raw_data()
        self.data = data_file(raw)
        self.data.create_database()

    """
# @brief   The method creates a window 
#          for setting the temperature.
# @param   None
# @return  None
    """
    def GUI_set_temp(self):
        self.temp_win = temp_GUI(self)
        self.temp_win.mainloop()

    """
# @brief   The method creates a window 
#          for setting the humidity.
# @param   None
# @return  None
    """
    def GUI_set_hum(self):
        self.hum_win = hum_GUI(self)
        self.hum_win.mainloop()

    """
# @brief   The method creates a window 
#          for setting the soil moisure.
# @param   None
# @return  None
    """
    def GUI_set_soil(self):
        self.soil_win = soil_GUI(self)
        self.soil_win.mainloop()

    """
# @brief   The method creates a window 
#          for setting the illumination.
# @param   None
# @return  None
    """    
    def GUI_set_ilu(self):
        self.ilu_win = ilu_GUI(self)
        self.ilu_win.mainloop()

    """
# @brief   The method creates a window 
#          for setting the time.
# @param   None
# @return  None
    """
    def GUI_set_time(self):
        self.time_win = time_GUI(self)
        self.time_win.mainloop()

    """
# @brief   The method creates a window 
#          for showing the graphical results.
# @param   None
# @return  None
    """
    def GUI_graph_res(self):
        self.graph_win = graph_GUI()
        self.graph_win.mainloop()

    """
# @brief   Callback function when the Connect button 
#          is pressed.
# @param   None
# @return  None
# @details The first press starts the communication. 
#          If successful, the button changes color 
#          to green and the text to RUN. 
#          Otherwise, it turns red.
#
#          A second press enables communication.
#          The button will change its text to Stop 
#          and its color to red.
#
#          A third press stops communication. 
#          The gray Connect button appears again.
    """
    def GUI_connect(self):
        # Communication is not started.
        if (self.phase == 0):
            # Try start communication.
            flat = self.start_serial()
            if (flat == 0):
                # Successful start.
                self.connect_but.configure(fg_color=self.color['run_col'],text="Run")
                self.phase = 1 # Communication was started.
            else:
                # Unseccessful start.
                self.connect_but.configure(fg_color=self.color['stop_col'],text="Connect")
                self.phase = 0 # Communication was stopped.

        # Communication is started.
        elif (self.phase == 1):
            self.connect_but.configure(fg_color=self.color['stop_col'],text="Stop")
            self.phase = 2     # Now communication is running.

        # Communication is running  
        elif (self.phase == 2):
            self.stop_serial() # Close serial communication.
            self.connect_but.configure(fg_color=self.color['gray'],text="Connect")
            self.phase = 0     # Now communication is stopped.

    """
# @brief   The function is started after entering the regulated values. 
#          The regulated values are displayed, saved in a data package and sent.
# @param   None
# @return  None
    """
    def update_settings(self):
        # Showing regulated data.
        update_show_settings(self)
        # Filling the data package.
        self.create_reg_packet()
        # Sending a data package.
        self.send_reg_packet()

    """
# @brief   The function displays the measured values in the main window.
# @param   None
# @return  None
    """
    def update_measure_value(self):
        # Showing temperature value.
        update_temp(self)
        # Showing humidity value.
        update_hum(self)
        # Showing soil moisure value.
        update_soil(self)
        # Showing illumination value.
        update_ilu(self)

    """
# @brief   Display of default data after startup.
# @param   None
# @return  None
    """
    def default_data(self):
        # Creating directories with default values.
        default_data(self)
        # Display of default values ​​of set regulated quantities.
        self.update_settings()
        # Display of default measured quantity values.
        self.update_measure_value()

    """
# @brief   If communication is running, it sends a packet with the time values.
# @param   None
# @return  None
    """
    def send_time_packet(self):
        if (self.phase == 2):
            self.send_message(self.time_packet)

    """
# @brief   If communication is running, it sends a packet with the regulation values.
# @param   None
# @return  None
    """
    def send_reg_packet(self):
        if (self.phase == 2):
            self.send_message(self.reg_packet)

    """
# @brief   Prepares a data package with regulations for sending.
# @param   None
# @return  None
    """
    def create_reg_packet(self):         
        full_reg_data(self)

    """
# @brief   Starts serial communication.
# @param   None
# @return  None
    """
    def start_serial(self):
        try:
            # It attempts to establish serial communication.
            self.serial_connection = serial.Serial(self.serial_port,self.baud_rate,timeout=1)
            # Creates a thread that will periodically check for data received by the serial port.
            self.serial_thread = threading.Thread(target=self.read_from_serial, daemon=True)
            self.serial_thread.start()
        except serial.SerialException as e:
            # Serial communication failed to start.
            return 1
        else: 
            # Serial communication was successfully started.
            return 0

    """
# @brief   Functions running on a separate thread. 
#          Reading, displaying and saving received data.
# @param   None
# @return  None
    """
    def read_from_serial(self):
        # The thread ends when communication is stopped.
        while self.running:
            # Communication exists, it doesn't wait and it runs.
            if self.serial_connection and self.serial_connection.in_waiting > 0 and self.phase == 2:
                try:
                    # Attempt to read a line.
                    line = self.serial_connection.readline()
                except Exception as e:
                    return
                else:
                    # The received data is stored in the raw_data object.
                    raw = raw_data()
                    for i in range (0,13,1):
                        raw.add(line[i])
                    # Processing received data.
                    self.data = data_file(raw)
                    # Saving received data.
                    self.measure_value['ilu'] = self.data.lig
                    self.measure_value['soil'] = self.data.soil
                    self.measure_value['hum'] = self.data.hum
                    self.measure_value['temp'] = self.data.temp
                    # Display received data.
                    self.update_measure_value()
                    # Adding received data to the database.
                    self.data.save_data()
            time.sleep(0.1)

    """
# @brief   The function ends serial communication.
# @param   None
# @return  None
    """
    def stop_serial(self):
        # The thread is stopped.
        self.running = False
        # If any communication existed and was ongoing, it is ended.
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

    """
# @brief   Sends a message via the serial port.
# @param   message Sent message.
# @return  None
    """    
    def send_message(self,message):
        # Communication exists and runs.
        if self.serial_connection and self.serial_connection.is_open:
            # Message must exist.
            if message:
                try:
                    # Attempt to send a message.
                    self.serial_connection.write(message)
                except Exception as e:
                    return
            #else:
                #return
        #else:
            #return
            
"""@}"""
