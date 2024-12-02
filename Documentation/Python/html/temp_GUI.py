"""
#############################################################
 # 
 # Class for creating a window for setting 
 # the temperature value and the hysteresis
 # of temperature .
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file temp_GUI
# @defgroup putala_win class GUI classes
# @code import temp_GUI @endcode
#
# @brief The class temp_GUI creates a pop-up window that allows 
#        you to set the  temperature value that will be 
#        regulated in the system. It also allows you 
#        to set hysteresis.
# 
# @details The pop-up window contains a line in which you can 
#          enter the desired temperature value and a line in which
#          you can enter the temperature hysteresis. It also contains 
#          the Apply and Close buttons. When you press Close, 
#          the window closes. 
#          When you press Apply, the text field is read. If 
#          the first line contains a numerical value between the 
#          minimum and maximum temperature values or the second line
#          contains a numerical value between minimum and maximum
#          temperature hysteresis, the set value is overwritten and 
#          the window closes.
#          Only correct input data are apply. 
#          If only one entry is valid, only one entry is applied.
#          Otherwise, the window does not close and the line contents
#          are deleted.
#
# @{


# Imports
import customtkinter as ckt # Custom Tkinter is used to create GUI.

class temp_GUI(ckt.CTk):

    def __init__(self,nmaster):
        """!
        @brief   Create window with two buttons
                 and two entry fields.
        @param   nmaster Window with main GUI.
        @return  None
        """
        super().__init__()
        self.master = nmaster
        self.createGUI()


    def apply(self):
        """!
        @brief   Sets the specified temperature value and temperature hysteresis.
        @param   None
        @return  None
        @details It reads from the temperature and hysteresis entry lines.
        """
        update = 0                      # At least one value can be changed.
        update = self.get_val()         # Read temperature value.
        self.get_hys(update)            # Read hysteresis.


    def get_val(self):
        """!
        @brief   Reads the set temperature value.
        @param   None
        @return  The set temperature value has been changed.
        @retval  0 - No change, 1 - Value has be changed.
        @details If the specified value is an int value and lies between 
                 temp_val_min and temp_val_max, the value will be set 
                 in the self.master.setting['temp_val'] directory.
        """
        try:
            temp = int(self.entry_00.get())    
        except:
            return 0
        else:
            if (temp <= self.master.system_setting['temp_val_max']) & (temp >= self.master.system_setting['temp_val_min']):
                self.master.setting['temp_val'] = temp
                return 1
            else:
                return 0

         
    def get_hys(self,update):
        """!
        @brief   Reads the set hysteresis value.
        @param   update Temperature value has changed.
        @return  None
        @details If the specified value is an int value and lies between 
                 temp_hys_min and temp_hys_max, the value will be set 
                 in the self.master.setting['temp_hys'] directory. The main window 
                 update is started. The allowed value is displayed in the main window.
                 The update will also take place if the hysteresis is not valid but 
                 the temperature value has changed.
        @note    If communication is running, this value will be written to 
                 the embedded device.
        """   
        try:
            temp = int(self.entry_01.get())    
        except:
            # Invalid hysteresis but value was changed. Not number.
            if update == 1:
                self.get_finish()
        else:
            if (temp <= self.master.system_setting['temp_hys_max']) & (temp >= self.master.system_setting['temp_hys_min']):
            # Valid hysteresis but value was changed.
                self.master.setting['temp_hys'] = temp
                self.get_finish()
            else:
            # Invalid hysteresis but value was changed. Out of range.
                if update == 1:
                    self.get_finish()


    def get_finish(self):
        """!
        @brief   Update data in main window and close
                 the window with temperature settings.
        @param   None
        @return  None
        """
        self.master.update_settings()
        self.destroy()


    def createGUI(self):
        """
        @brief   Create GUI for temperature settings.
                 Set size and title of the window.
                 Window is not resizable.
        @param   None
        @return  None
        """
        self.title('Temperature settings')
        self.geometry("300x150")
        self.resizable(False,False)

        """! Create inscription Temperature in the window."""
        self.txtfield_00 = ckt.CTkLabel(master=self,text='Temperature (°C):',width=20,font=('Arial',20))
        self.txtfield_00.place(relx=0.1,rely=0.2,anchor='w')

        """! Create inscription Hysteresis in the window."""
        self.txtfield_01 = ckt.CTkLabel(master=self,text='Hysteresis (°C):',width=20,font=('Arial',20))
        self.txtfield_01.place(relx=0.1,rely=0.45,anchor='w')

        """! Create Apply button. It has callback function self.apply."""
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=80,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.65)

        """! Create Close button. Press to destroy window."""
        self.but02 = ckt.CTkButton(master=self,text='Close',width=80,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.65)

        """! Create entry field in the window. Required temperature value can be written here."""
        self.entry_00=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['temp_val']),
                                   width=70,font=('Arial',20))
        self.entry_00.place(relx=0.72,rely=0.2,anchor='w')

        """! Create entry field in the window. Required temperature hysteresis can be written here."""
        self.entry_01=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['temp_hys']),
                                   width=70,font=('Arial',20))
        self.entry_01.place(relx=0.72,rely=0.45,anchor='w')

##@}