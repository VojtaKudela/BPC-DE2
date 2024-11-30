"""
#############################################################
 # 
 # Class for creating a window for setting 
 # the soil moisure value and the hysteresis
 # of soil moisure.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win class soil_GUI
 # @code import soil_GUI @endcode
 #
 # @brief The class creates a pop-up window that allows 
 #        you to set the soil moisure value that will be 
 #        regulated in the system. It also allows you 
 #        to set hysteresis.
 # 
 # @details The pop-up window contains a line in which you can 
 #          enter the desired soil moisure value and a line in which
 #          you can enter the soil moisure hysteresis. It also contains 
 #          the Apply and Close buttons. When you press Close, 
 #          the window closes. 
 #          When you press Apply, the text field is read. If 
 #          the first line contains a numerical value between the 
 #          minimum and maximum soil moisure values or the second line
 #          contains a numerical value between minimum and maximum
 #          soil moisure hysteresis, the set value is overwritten and 
 #          the window closes.
 #          Only correct input data are apply. 
 #          If only one entry is valid, only one entry is applied.
 #          Otherwise, the window does not close and the line contents
 #          are deleted.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

# Imports
import customtkinter as ckt # Custom Tkinter is used to create GUI.

class soil_GUI(ckt.CTk):
    """
# @brief   Create window with two buttons
#          and two entry fields.
# @param   nmaster Window with main GUI.
# @return  None
    """
    def __init__(self,nmaster):
        super().__init__()
        self.master = nmaster
        self.createGUI()

    """
# @brief   Sets the specified soil moisure value and soil moisure hysteresis.
# @param   None
# @return  None
# @details It reads from the soil moisure and hysteresis entry lines.
    """
    def apply(self):
        update = 0                      # At least one value can be changed.
        update = self.get_val()         # Read soil moisure value.
        self.get_hys(update)            # Read hysteresis.

    """
# @brief   Reads the set soil moisure value.
# @param   None
# @return  The set soil moisure value has been changed.
# @retval  0 - No change, 1 - Value has be changed.
# @details If the specified value is an int value and lies between 
#          soil_val_min and soil_val_max, the value will be set 
#          in the self.master.setting['soil_val'] directory.
    """
    def get_val(self):
        try:
            temp = int(self.entry_00.get())    
        except:
            return 0
        else:
            if (temp <= self.master.system_setting['soil_val_max']) & (temp >= self.master.system_setting['soil_val_min']):
                self.master.setting['soil_val'] = temp
                return 1
            else:
                return 0

    """
# @brief   Reads the set hysteresis value.
# @param   update Soil moisure value has changed.
# @return  None
# @details If the specified value is an int value and lies between 
#          soil_hys_min and soil_hys_max, the value will be set 
#          in the self.master.setting['soil_hys'] directory. The main window 
#          update is started. The allowed value is displayed in the main window.
#          The update will also take place if the hysteresis is not valid but 
#          the soil moisure value has changed.
# @note    If communication is running, this value will be written to 
#          the embedded device.
    """            
    def get_hys(self,update):
        try:
            temp = int(self.entry_01.get())    
        except:
            # Invalid hysteresis but value was changed. Not number.
            if update == 1:
                self.get_finish()
        else:
            if (temp <= self.master.system_setting['soil_hys_max']) & (temp >= self.master.system_setting['soil_hys_min']):
            # Valid hysteresis but value was changed.
                self.master.setting['soil_hys'] = temp
                self.get_finish()
            else:
            # Invalid hysteresis but value was changed. Out of range.
                if update == 1:
                    self.get_finish()

    """
# @brief   Update data in main window and close
#          the window with soil moisure settings.
# @param   None
# @return  None
    """
    def get_finish(self):
        self.master.update_settings()
        self.destroy()

    """
# @brief   Create GUI for soil moisure settings.
#          Set size and title of the window.
#          Window is not resizable.
# @param   None
# @return  None
    """
    def createGUI(self):
        self.title('Soil moisure settings')
        self.geometry("300x150")
        self.resizable(False,False)

        """Create inscription Soil moisure in the window."""
        self.txtfield_00 = ckt.CTkLabel(master=self,text='Soil moisure (%):',width=20,font=('Arial',20))
        self.txtfield_00.place(relx=0.1,rely=0.2,anchor='w')

        """Create inscription Hysteresis in the window."""
        self.txtfield_01 = ckt.CTkLabel(master=self,text='Hysteresis (%):',width=20,font=('Arial',20))
        self.txtfield_01.place(relx=0.1,rely=0.45,anchor='w')

        """ Create Apply button. It has callback function self.apply."""
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=80,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.65)

        """ Create Close button. Press to destroy window."""
        self.but02 = ckt.CTkButton(master=self,text='Close',width=80,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.65)

        """Create entry field in the window. Required soil moisure value can be written here."""
        self.entry_00=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['soil_val']),
                                   width=70,font=('Arial',20))
        self.entry_00.place(relx=0.72,rely=0.2,anchor='w')

        """Create entry field in the window. Required soil moisure hysteresis can be written here."""
        self.entry_01=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['soil_hys']),
                                   width=70,font=('Arial',20))
        self.entry_01.place(relx=0.72,rely=0.45,anchor='w')

"""@}"""