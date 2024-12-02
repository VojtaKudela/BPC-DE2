"""
#############################################################
 # 
 # Function for creating regulation settings GUI.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_createGUI Function for creating GUI
# @code import createGUIset @endcode
#
# @brief The function createGUIset creates a GUI for regulation of temperature,
#        humidity, soil moisure and illumination.
#
# @details A panel will be created in the upper right corner of 
#          the self. The panel will contain four buttons: 
#          Set temperature, Set humidity, Set soil moisture and 
#          Set illumination. The panel will also display the 
#          set values including hysteresis.
#
# @{

# Imports
import customtkinter as ckt # Custom Tkinter is used to create GUI.

def createGUIset(self):
    # It creates a panel in which the buttons will be placed. 
    # The panel contains the inscription Settings.
    self.reg_frame = ckt.CTkFrame(master=self,width=500,height=200,fg_color=self.color['pink'])
    self.reg_frame.place(relx=0.69, rely=0.2, anchor="center")

    self.txt_set = ckt.CTkLabel(master=self.reg_frame,text="Settings:",font=("Arial",24))
    self.txt_set.place(relx=0.15, rely=0.12, anchor="center")

    # It creates a Set temperature button. It will also create a text field that will contain 
    # information about the currently set value. Button has s callback function self.GUI_set_temp.
    self.txt_set_temp = ckt.CTkLabel(master=self.reg_frame,text="Temperature:",font=("Arial",20))
    self.txt_set_temp.place(relx=0.18, rely=0.32, anchor="center")

    self.txt_set_temp_value = ckt.CTkLabel(master=self.reg_frame,text="27°C ± 1°C",font=("Arial",20))
    self.txt_set_temp_value.place(relx=0.52, rely=0.32, anchor="center")

    self.txt_set_temp_but = ckt.CTkButton(master=self.reg_frame,text="Set temperature",
                                          font=("Arial",20),width=160,height=25,fg_color=self.color['red'],
                                          command=self.GUI_set_temp)
    self.txt_set_temp_but.place(relx=0.82, rely=0.32, anchor="center")

    # It creates a Set humidity button. It will also create a text field that will contain 
    # information about the currently set value. Button has s callback function self.GUI_set_hum.
    self.txt_set_hum = ckt.CTkLabel(master=self.reg_frame,text="Humidity:",font=("Arial",20))
    self.txt_set_hum.place(relx=0.148, rely=0.52, anchor="center")

    self.txt_set_hum_value = ckt.CTkLabel(master=self.reg_frame,text="50 % ± 5 %",font=("Arial",20))
    self.txt_set_hum_value.place(relx=0.52, rely=0.52, anchor="center")

    self.txt_set_hum_but = ckt.CTkButton(master=self.reg_frame,text="Set humidity",
                                         font=("Arial",20),width=160,height=25,fg_color=self.color['blue'],
                                         command=self.GUI_set_hum)
    self.txt_set_hum_but.place(relx=0.82, rely=0.52, anchor="center")

    # It creates a Set soil moisure button. It will also create a text field that will contain 
    # information about the currently set value. Button has s callback function self.GUI_set_soil.
    self.txt_set_soil = ckt.CTkLabel(master=self.reg_frame,text="Soil Moisure:",font=("Arial",20))
    self.txt_set_soil.place(relx=0.18, rely=0.72, anchor="center")

    self.txt_set_soil_value = ckt.CTkLabel(master=self.reg_frame,text="57 % ± 5 %",font=("Arial",20))
    self.txt_set_soil_value.place(relx=0.52, rely=0.72, anchor="center")

    self.txt_set_soil_but = ckt.CTkButton(master=self.reg_frame,text="Set soil moisure",
                                          font=("Arial",20),width=160,height=25,fg_color=self.color['cyan'],
                                          command=self.GUI_set_soil)
    self.txt_set_soil_but.place(relx=0.82, rely=0.72, anchor="center")

    # It creates a Set illumination button. It will also create a text field that will contain 
    # information about the currently set value. Button has s callback function self.GUI_set_ilu.
    self.txt_set_ilu = ckt.CTkLabel(master=self.reg_frame,text="Illumination:",font=("Arial",20))
    self.txt_set_ilu.place(relx=0.175, rely=0.92, anchor="center")

    self.txt_set_ilu_value = ckt.CTkLabel(master=self.reg_frame,text="200 lx",font=("Arial",20))
    self.txt_set_ilu_value.place(relx=0.52, rely=0.92, anchor="center")

    self.txt_set_ilu_but = ckt.CTkButton(master=self.reg_frame,text="Set illumination",
                                         font=("Arial",20),width=160,height=25,fg_color=self.color['gold'],
                                         command=self.GUI_set_ilu)
    self.txt_set_ilu_but.place(relx=0.82, rely=0.92, anchor="center")

##@}