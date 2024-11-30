
import customtkinter as ckt

class soil_GUI(ckt.CTk):
    def __init__(self,nmaster):
        super().__init__()
        self.master = nmaster
        self.createGUI()

    def apply(self):
        update = 0
        update = self.get_val(update)
        self.get_hys(update)

    def get_val(self,update):
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
            
    def get_hys(self,update):
        try:
            temp = int(self.entry_01.get())    
        except:
            if update == 1:
                self.get_finish()
        else:
            if (temp <= self.master.system_setting['soil_hys_max']) & (temp >= self.master.system_setting['soil_hys_min']):
                self.master.setting['soil_hys'] = temp
                self.get_finish()
            else:
                if update == 1:
                    self.get_finish()

    def get_finish(self):
        self.master.update_settings()
        self.destroy()

    def createGUI(self):
        self.title('Soil moisure settings')
        self.geometry("300x150")
        self.resizable(False,False)
        self.txtfield_00 = ckt.CTkLabel(master=self,text='Soil moisure (%):',width=20,font=('Arial',20))
        self.txtfield_00.place(relx=0.1,rely=0.2,anchor='w')
        self.txtfield_01 = ckt.CTkLabel(master=self,text='Hysteresis (%):',width=20,font=('Arial',20))
        self.txtfield_01.place(relx=0.1,rely=0.45,anchor='w')
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=80,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.65)
        self.but02 = ckt.CTkButton(master=self,text='Close',width=80,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.65)
        self.entry_00=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['soil_val']),width=70,font=('Arial',20))
        self.entry_00.place(relx=0.72,rely=0.2,anchor='w')
        self.entry_01=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['soil_hys']),width=70,font=('Arial',20))
        self.entry_01.place(relx=0.72,rely=0.45,anchor='w')
