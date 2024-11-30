"""
#############################################################
 # 
 # Function for creating main settings GUI.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_createGUI func createGUImain
 # @code import createGUImain @endcode
 #
 # @brief The function creates a GUI for connecting, setting the time, 
 #        and displaying graphical results.
 #
 # @details The function creates three buttons in the upper left 
 #          corner of the self: Connect, Set time, and Graphical results.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""
# Imports
import customtkinter as ckt # Custom Tkinter is used to create GUI.

def createGUImain(self):
    """ Create button for connection. It has callback function self.GUI_connect."""
    self.connect_but = ckt.CTkButton(master=self,text="Connect",font=("Arial",24),width=200,height=25,fg_color=self.color['gray'],text_color=self.color['black'],command=self.GUI_connect)
    self.connect_but.place(relx=0.18, rely=0.1, anchor="center")

    """ Create button for time setting. It has callback function self.GUI_set_time. """
    self.set_time_but = ckt.CTkButton(master=self,text="Set time",font=("Arial",24),width=200,height=25,fg_color=self.color['gray'],text_color=self.color['black'],command=self.GUI_set_time)
    self.set_time_but.place(relx=0.18, rely=0.2, anchor="center")

    """ Create button for showing graphical results. It has callback function self.GUI_graph_res."""
    self.set_graph_but = ckt.CTkButton(master=self,text="Graphical results",font=("Arial",24),width=200,height=25,fg_color=self.color['gray'],text_color=self.color['black'],command=self.GUI_graph_res)
    self.set_graph_but.place(relx=0.18, rely=0.3, anchor="center")

"""@}"""