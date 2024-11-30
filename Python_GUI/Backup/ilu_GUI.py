
import customtkinter as ckt

class ilu_GUI(ckt.CTk):
    def __init__(self,nmaster):
        super().__init__()
        self.master = nmaster
        self.createGUI()

    def apply(self):
        try:
            temp = int(self.entry.get())    
        except:
            return
        else:
            if (temp <= self.master.system_setting['ilu_max']) & (temp >= self.master.system_setting['ilu_min']):
                self.master.setting['ilu_val'] = temp
                self.master.update_settings()
                self.destroy()

    def createGUI(self):
        self.title('Illumination settings')
        self.geometry("300x100")
        self.resizable(False,False)
        self.txtfield = ckt.CTkLabel(master=self,text='Illumination (lx):',width=20,font=('Arial',20))
        self.txtfield.place(relx=0.1,rely=0.25,anchor='w')
        self.but01 = ckt.CTkButton(master=self,text='Apply',width=80,command=self.apply,font=('Arial',20))
        self.but01.place(relx=0.40,rely=0.5)
        self.but02 = ckt.CTkButton(master=self,text='Close',width=80,command=self.destroy,font=('Arial',20))
        self.but02.place(relx=0.7,rely=0.5)
        self.entry=ckt.CTkEntry(master=self,placeholder_text=str(self.master.setting['ilu_val']),width=70,font=('Arial',20))
        self.entry.place(relx=0.72,rely=0.25,anchor='w')

#win = ilu_GUI()
#win.mainloop()
