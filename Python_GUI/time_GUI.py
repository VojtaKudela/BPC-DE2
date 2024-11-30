"""
#############################################################
 # 
 # Class for creating a window for time setting.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win class time_GUI
 # @code import time_GUI @endcode
 #
 # @brief The class creates a window for setting the time. The window 
 #        allows you to set the year, month, date, day of the week, 
 #        hour, minute, and second.
 # 
 # @details The window contains two buttons: Apply and Close. Pressing 
 #          the Close button closes the window. Pressing the Apply button 
 #          reads all the set values and, if they are correct, prepares 
 #          the data for sending and closes the window. Otherwise, 
 #          it deletes the set values.
 #
 #          The window also contains a drop-down menu for selecting 
 #          the year, month, day of the week and hour, and an entry text 
 #          field for entering the date, minutes and seconds.
 # 
 # @note    If communication is running, this value will be written to 
 #          the embedded device.
 #
 # @warning The data will be sent and the window will be closed provided 
 #          that all entered data is valid.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

# Imports
import customtkinter as ckt       # Custom Tkinter is used to create GUI.
from month2num import month2num   # Converting the name of the month to its order.
from num_and_days import day2num  # Converting the name of the day of the week to its order.

class time_GUI(ckt.CTk):
    """
# @brief   Create window with two buttons, 
#          four drop-down menus and three 
#          entry fields.
# @param   nmaster Window with main GUI.
# @return  None
    """
    def __init__(self,nmaster):
        super().__init__()
        self.master = nmaster
        self.createGUI()

    """
# @brief   It reads, checks and prepares the entered time 
#          for sending. If the data is valid, it closes 
#          the window. Otherwise, it deletes the entered values.
# @param   None
# @return  None
    """
    def apply(self):
        ## Get year. Only the last two digits are processed.
        try:
            year = int(self.entry_year.get())-2000
        except:
            return
        else:
            ## Get month.
            month = month2num(self.entry_month.get())
            if (month > 12):
                return
            
            ## Get day in the week.
            day = self.entry_day.get()
            if (day == ""):
                return
            day = day2num(day[0:2]) # Funcion processes the first two letters.

            ## Get date. Entry data must be integer.
            try:
                date = int(self.entry_date.get())
            except:
                # Not integer.
                return
            else:

                ## Number of days in months varies.
                if (date < 1):
                    return
                # No month has more than 31 days.
                if (date > 31):
                    return
                # February outside of leap years.
                if (date > 28) & (month == 2) & (year%4 != 0):
                    return
                # February in general (leap and standard years).
                if (date > 29) & (month == 2):
                    return
                # April, June, September and November have 30 days.
                if (date > 30) & ((month == 4) | (month == 6) | (month == 9) | (month == 11)):
                    return
                
                ## Get hour.
                hour = self.entry_hour.get()
                if (hour == ""):
                    return
                # Hour must be integer in the range of 0 to 23.
                hour = int(hour)
                if (hour > 23) | (hour < 0):
                    return
                
                # Get minute. Minute must be integer.
                try:
                    minute = int(self.entry_minute.get())
                except:
                    # Not integer.
                    return
                else:
                    # Minute must be in the range of 0 to 59.
                    if (minute < 0) | (minute > 59):
                        return
                    
                    ## Get second. Second must be integer.
                    try:
                        second = int(self.entry_second.get())
                    except:
                        # Not integer.
                        return
                    else:
                        # Second must be in the range of 0 to 59.
                        if (second < 0) | (second > 59):
                            return

                        # Null time packet. The first byte remains 'T'.
                        for i in range(1,8,1):
                            self.master.time_packet[i] = 0x00

                        #### Create time packet. ####
                        # The tens of the year are stored in the higher nibble and the units in the lower nibble.
                        self.master.time_packet[1] |= (((year//10)<<4) | (year%10))
                        # The tens of the month are stored in the higher nibble and the units in the lower nibble.
                        # The MSB carry information about century. 0 - 20th, 1 - 21th.
                        self.master.time_packet[2] |= (1 << 7) | (((month//10)<<4) | (month%10))
                        # The tens of the date are stored in the higher nibble and the units in the lower nibble.
                        self.master.time_packet[3] |= (((date//10)<<4) | (date%10))
                        # The day of the week corresponds to the number 0 - 6.
                        self.master.time_packet[4] |= day
                        # The tens of the hour are stored in the higher nibble and the units in the lower nibble.
                        self.master.time_packet[5] |= (((hour//10)<<4) | (hour%10))
                        # The tens of the minute are stored in the higher nibble and the units in the lower nibble.
                        self.master.time_packet[6] |= (((minute//10)<<4) | (minute%10))
                        # The tens of the second are stored in the higher nibble and the units in the lower nibble.
                        self.master.time_packet[7] |= (((second//10)<<4) | (second%10))

                        ## Send data
                        self.master.send_time_packet()
                        self.destroy()               
                
        """
# @brief   Create GUI for time settings.
#          Set size and title of the window.
#          Window is not resizable.
# @param   None
# @return  None
    """
    def createGUI(self):
        self.title('Time settings')
        self.geometry("500x200")
        self.resizable(False,False)

        """Create inscription Year in the window."""
        self.txtfield_year = ckt.CTkLabel(master=self,text='Year:',width=20,font=('Arial',20))
        self.txtfield_year.place(relx=0.07,rely=0.15,anchor='w')

        """Create inscription Month in the window."""
        self.txtfield_month = ckt.CTkLabel(master=self,text='Month:',width=20,font=('Arial',20))
        self.txtfield_month.place(relx=0.07,rely=0.3,anchor='w')

        """Create inscription Date in the window."""
        self.txtfield_date = ckt.CTkLabel(master=self,text='Date:',width=20,font=('Arial',20))
        self.txtfield_date.place(relx=0.07,rely=0.45,anchor='w')

        """Create inscription Day in the window."""
        self.txtfield_day = ckt.CTkLabel(master=self,text='Day:',width=20,font=('Arial',20))
        self.txtfield_day.place(relx=0.07,rely=0.6,anchor='w')

        """Create inscription Hour in the window."""
        self.txtfield_hour = ckt.CTkLabel(master=self,text='Hour:',width=20,font=('Arial',20))
        self.txtfield_hour.place(relx=0.52,rely=0.15,anchor='w')

        """Create inscription Minute in the window."""
        self.txtfield_minute = ckt.CTkLabel(master=self,text='Minute:',width=20,font=('Arial',20))
        self.txtfield_minute.place(relx=0.52,rely=0.3,anchor='w')

        """Create inscription Second in the window."""
        self.txtfield_second = ckt.CTkLabel(master=self,text='Second:',width=20,font=('Arial',20))
        self.txtfield_second.place(relx=0.52,rely=0.45,anchor='w')

        """ Create Apply button. It has callback function self.apply."""
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=120,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.75)

        """ Create Close button. Press to destroy window."""
        self.but02 = ckt.CTkButton(master=self,text='Close',width=120,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.75)

        """Creates a drop-down menu for selecting a year in the window."""
        self.entry_year=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',
                                        values=['2024','2025','2026','2027','2028','2029','2030',
                                                '2031','2032','2033','2034','2035','2036','2037','2038',
                                                '2039','2040','2041','2042','2043','2044','2045','2046',
                                                '2047','2048','2049','2050'])
        self.entry_year.place(relx=0.21,rely=0.15,anchor='w')

        """Creates a drop-down menu for selecting a month in the window. Direct entry is prohibited."""
        self.entry_month=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',
                                         values=['January','February','March','April','May','June',
                                                 'July','August','September','October','November','December'])
        self.entry_month.place(relx=0.21,rely=0.3,anchor='w')

        """Create entry field in the window. Required date shall be written here."""
        self.entry_date=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=1)
        self.entry_date.place(relx=0.21,rely=0.45,anchor='w')

        """Creates a drop-down menu for selecting a day in the window. Direct entry is prohibited."""
        self.entry_day=ckt.CTkComboBox(master=self,width=180,font=('Arial',20),state='readonly',
                                       values=['Monday','Tuesday','Wednesday','Thursday','Friday',
                                               'Saturday','Sunday'])
        self.entry_day.place(relx=0.21,rely=0.6,anchor='w')

        """Creates a drop-down menu for selecting a hour in the window. Direct entry is prohibited."""
        self.entry_hour=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',
                                        values=["0","1","2","3","4","5","6","7","8","9","10","11",
                                                "12","13","14","15","16","17","18","19","20","21","22","23"])
        self.entry_hour.place(relx=0.69,rely=0.15,anchor='w')

        """Create entry field in the window. Required minute shall be written here."""
        self.entry_minute=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=0)
        self.entry_minute.place(relx=0.69,rely=0.3,anchor='w')

        """Create entry field in the window. Required second shall be written here."""
        self.entry_second=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=0)
        self.entry_second.place(relx=0.69,rely=0.45,anchor='w')

"""@}"""