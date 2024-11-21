
import customtkinter as ckt
from month2num import month2num
from num_and_days import day2num

class time_GUI(ckt.CTk):
    def __init__(self,nmaster):
        super().__init__()
        self.master = nmaster
        self.createGUI()

## Callback of APPLY button
    def apply(self):
    ## Get year
        try:
            year = int(self.entry_year.get())-2000
        except:
            return
        else:
    ## Get month
            month = month2num(self.entry_month.get())
            if (month > 12):
                return
            
    ## Get day
            day = self.entry_day.get()
            if (day == ""):
                return
            day = day2num(day[0:2])
    ## Get date
            try:
                date = int(self.entry_date.get())
            except:
                return
            else:
        ## Number of days in months varies.
                if (date < 1):
                    return
                if (date > 31):
                    return
                if (date > 28) & (month == 2) & (year%4 != 0):
                    return
                if (date > 29) & (month == 2):
                    return
                if (date > 30) & ((month == 4) | (month == 6) | (month == 9) | (month == 11)):
                    return
                
    ## Get hour
                hour = self.entry_hour.get()
                if (hour == ""):
                    return
                hour = int(hour)
                if (hour > 23) | (hour < 0):
                    return
    # Get minute
                try:
                    minute = int(self.entry_minute.get())
                except:
                    return
                else:
                    if (minute < 0) | (minute > 59):
                        return
    ## Get second
                    try:
                        second = int(self.entry_second.get())
                    except:
                        return
                    else:
                        if (second < 0) | (second > 59):
                            return

    ## Null time packet
                        for i in range(1,8,1):
                            self.master.time_packet[i] = 0x00

    ## Create time packet
                        self.master.time_packet[1] |= (((year//10)<<4) | (year%10))
                        self.master.time_packet[2] |= (((month//10)<<4) | (month%10))
                        self.master.time_packet[3] |= (((date//10)<<4) | (date%10))
                        self.master.time_packet[4] |= day
                        self.master.time_packet[5] |= (((hour//10)<<4) | (hour%10))
                        self.master.time_packet[6] |= (((minute//10)<<4) | (minute%10))
                        self.master.time_packet[7] |= (((second//10)<<4) | (second%10))

    ## Send data
                        self.master.send_time_packet()
                        self.destroy()               
                



    def createGUI(self):
        self.title('Time settings')
        self.geometry("500x200")
        self.resizable(False,False)

        self.txtfield_year = ckt.CTkLabel(master=self,text='Year:',width=20,font=('Arial',20))
        self.txtfield_year.place(relx=0.07,rely=0.15,anchor='w')

        self.txtfield_month = ckt.CTkLabel(master=self,text='Month:',width=20,font=('Arial',20))
        self.txtfield_month.place(relx=0.07,rely=0.3,anchor='w')

        self.txtfield_date = ckt.CTkLabel(master=self,text='Date:',width=20,font=('Arial',20))
        self.txtfield_date.place(relx=0.07,rely=0.45,anchor='w')

        self.txtfield_day = ckt.CTkLabel(master=self,text='Day:',width=20,font=('Arial',20))
        self.txtfield_day.place(relx=0.07,rely=0.6,anchor='w')

        self.txtfield_hour = ckt.CTkLabel(master=self,text='Hour:',width=20,font=('Arial',20))
        self.txtfield_hour.place(relx=0.52,rely=0.15,anchor='w')

        self.txtfield_minute = ckt.CTkLabel(master=self,text='Minute:',width=20,font=('Arial',20))
        self.txtfield_minute.place(relx=0.52,rely=0.3,anchor='w')

        self.txtfield_second = ckt.CTkLabel(master=self,text='Second:',width=20,font=('Arial',20))
        self.txtfield_second.place(relx=0.52,rely=0.45,anchor='w')

        self.but01 = ckt.CTkButton(master=self,text='Apply',width=120,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.75)

        self.but02 = ckt.CTkButton(master=self,text='Close',width=120,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.75)

        self.entry_year=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',values=['2024','2025','2026','2027','2028','2029','2030','2031','2032','2033','2034','2035','2036','2037','2038','2039','2040','2041','2042','2043','2044','2045','2046','2047','2048','2049','2050'])
        self.entry_year.place(relx=0.21,rely=0.15,anchor='w')

        self.entry_month=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',values=['January','February','March','April','May','June','July','August','September','October','November','December'])
        self.entry_month.place(relx=0.21,rely=0.3,anchor='w')

        self.entry_date=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=1)
        self.entry_date.place(relx=0.21,rely=0.45,anchor='w')

        self.entry_day=ckt.CTkComboBox(master=self,width=180,font=('Arial',20),state='readonly',values=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
        self.entry_day.place(relx=0.21,rely=0.6,anchor='w')

        self.entry_hour=ckt.CTkComboBox(master=self,width=140,font=('Arial',20),state='readonly',values=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"])
        self.entry_hour.place(relx=0.69,rely=0.15,anchor='w')

        self.entry_minute=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=0)
        self.entry_minute.place(relx=0.69,rely=0.3,anchor='w')

        self.entry_second=ckt.CTkEntry(master=self,width=140,font=('Arial',20),placeholder_text=0)
        self.entry_second.place(relx=0.69,rely=0.45,anchor='w')