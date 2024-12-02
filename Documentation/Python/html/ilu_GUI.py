"""
#############################################################
 # 
 # Class for creating a window for setting 
 # the illumination value.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_win GUI classes
# @code import ilu_GUI @endcode
#
# @brief The class ilu_GUI creates a pop-up window that allows 
#        you to set the illumination value that will be 
#        regulated in the system.
# 
# @details The pop-up window contains a line in which you can 
#          enter the desired illumination value. It also contains 
#          the Apply and Close buttons. When you press Close, 
#          the window closes. 
#          When you press Apply, the text field is read. If 
#          the line contains a numerical value between the 
#          minimum and maximum lighting values, the set value 
#          is overwritten and the window closes. Otherwise, 
#          the window does not close and the line content 
#          is deleted.
#
# @{

# Imports
import customtkinter as ckt # Custom Tkinter is used to create GUI.


class ilu_GUI(ckt.CTk):

    def __init__(self,nmaster):
        """!
        @brief   Create window with two buttons
                 and one entry field.
        @param   nmaster Window with main GUI.
        @return  None
        """
        super().__init__()
        self.master = nmaster
        self.createGUI()


    def apply(self):
        """!
        @brief   Sets the specified illumination value.
        @param   None
        @return  None
        @details If the specified value is an int value and lies between 
                 ilu_min and ilu_max, the value will be set 
                 in the self.master.setting['ilu_val'] directory. The main window 
                 update is started. The allowed value is displayed in the main window.
        @note    If communication is running, this value will be written to 
                 the embedded device.
    """
        try:
            temp = int(self.entry.get())    
        except:
            return
        else:
            # Set value must be in allowed range.
            if (temp <= self.master.system_setting['ilu_max']) & (temp >= self.master.system_setting['ilu_min']):
                # Storage illumination value to main window data file.
                self.master.setting['ilu_val'] = temp
                # Update main window.
                self.master.update_settings()
                # Close illumination window.
                self.destroy()


    def createGUI(self):
        """!
        @brief   Create GUI for illumination settings.
                 Set size and title of the window.
                 Window is not resizable.
        @param   None
        @return  None
        """
        self.title('Illumination settings')
        self.geometry("300x100")
        self.resizable(False,False)

        """! Create inscription Illumination in the window."""
        self.txtfield = ckt.CTkLabel(master=self,text='Illumination (lx):',width=20,font=('Arial',20))
        self.txtfield.place(relx=0.1,rely=0.25,anchor='w')

        """! Create Apply button. It has callback function self.apply."""
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=80,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.5)

        """! Create Close button. Press to destroy window."""
        self.but02 = ckt.CTkButton(master=self,text='Close',width=80,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.5)

        """! Create entry field in the window. Required illumination value can be written here."""
        self.entry=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['ilu_val']),width=70,
                                font=('Arial',20))
        self.entry.place(relx=0.72,rely=0.25,anchor='w')

##@}