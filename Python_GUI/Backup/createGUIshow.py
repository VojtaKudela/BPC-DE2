
import customtkinter as ckt
import tkinter as tk

def createGUIshow(self):
    # Panel
    self.show_frame = ckt.CTkFrame(master=self,width=1600,height=300,fg_color='#84FFBA')
    self.show_frame.place(relx=0, rely=0.7, anchor="center")

    # Temperature
    self.txt_temp = ckt.CTkLabel(master=self.show_frame,text="Temperature",font=("Arial",20))
    self.txt_temp.place(relx=0.55, rely=0.12, anchor="center")

    self.temp_progress = ckt.CTkProgressBar(self.show_frame,orientation="vertical",width=20,height=180,progress_color='#FF4444')
    self.temp_progress.place(relx=0.55, rely=0.50, anchor="center")

    self.txt_temp = ckt.CTkLabel(master=self.show_frame,text="25.1°C",font=("Arial",24),bg_color='#DDDDFF',width=60,height=40,corner_radius=10)
    self.txt_temp.place(relx=0.55, rely=0.9, anchor="center")

    self.txt_temp_15 = ckt.CTkLabel(master=self.show_frame,text="15-",font=("Arial",20))
    self.txt_temp_15.place(relx=0.535, rely=0.74, anchor="center")

    self.txt_temp_30 = ckt.CTkLabel(master=self.show_frame,text="30-",font=("Arial",20))
    self.txt_temp_30.place(relx=0.535, rely=0.57, anchor="center")

    self.txt_temp_45 = ckt.CTkLabel(master=self.show_frame,text="45-",font=("Arial",20))
    self.txt_temp_45.place(relx=0.535, rely=0.40, anchor="center")

    self.txt_temp_60 = ckt.CTkLabel(master=self.show_frame,text="60-",font=("Arial",20))
    self.txt_temp_60.place(relx=0.535, rely=0.23, anchor="center")

    self.txt_temp_unit = ckt.CTkLabel(master=self.show_frame,text="°C",font=("Arial",32))
    self.txt_temp_unit.place(relx=0.570, rely=0.23, anchor="center")

    # Humidity
    self.txt_hum = ckt.CTkLabel(master=self.show_frame,text="Humidity",font=("Arial",20))
    self.txt_hum.place(relx=0.68, rely=0.12, anchor="center")

    self.hum_progress = ckt.CTkProgressBar(self.show_frame,orientation="vertical",width=20,height=180,progress_color='#4444FF')
    self.hum_progress.place(relx=0.68, rely=0.50, anchor="center")

    self.txt_hum = ckt.CTkLabel(master=self.show_frame,text="56.1%",font=("Arial",24),bg_color='#DDDDFF',width=60,height=40,corner_radius=10)
    self.txt_hum.place(relx=0.68, rely=0.9, anchor="center")

    self.txt_hum_0 = ckt.CTkLabel(master=self.show_frame,text="0-",font=("Arial",20))
    self.txt_hum_0.place(relx=0.668, rely=0.77, anchor="center")

    self.txt_hum_33 = ckt.CTkLabel(master=self.show_frame,text="33-",font=("Arial",20))
    self.txt_hum_33.place(relx=0.665, rely=0.59, anchor="center")

    self.txt_hum_67 = ckt.CTkLabel(master=self.show_frame,text="67-",font=("Arial",20))
    self.txt_hum_67.place(relx=0.665, rely=0.41, anchor="center")

    self.txt_hum_100 = ckt.CTkLabel(master=self.show_frame,text="100-",font=("Arial",20))
    self.txt_hum_100.place(relx=0.6615, rely=0.23, anchor="center")

    self.txt_hum_unit = ckt.CTkLabel(master=self.show_frame,text="%",font=("Arial",32))
    self.txt_hum_unit.place(relx=0.700, rely=0.23, anchor="center")

    # Soil Moisure
    self.txt_soil = ckt.CTkLabel(master=self.show_frame,text="Soil moisture",font=("Arial",20))
    self.txt_soil.place(relx=0.81, rely=0.12, anchor="center")

    self.soil_progress = ckt.CTkProgressBar(self.show_frame,orientation="vertical",width=20,height=180,progress_color='#7777FF')
    self.soil_progress.place(relx=0.81, rely=0.50, anchor="center")

    self.txt_soil = ckt.CTkLabel(master=self.show_frame,text="54.1%",font=("Arial",24),bg_color='#DDDDFF',width=60,height=40,corner_radius=10)
    self.txt_soil.place(relx=0.81, rely=0.9, anchor="center")

    self.txt_soil_0 = ckt.CTkLabel(master=self.show_frame,text="0-",font=("Arial",20))
    self.txt_soil_0.place(relx=0.798, rely=0.77, anchor="center")

    self.txt_soil_33 = ckt.CTkLabel(master=self.show_frame,text="33-",font=("Arial",20))
    self.txt_soil_33.place(relx=0.795, rely=0.59, anchor="center")

    self.txt_soil_67 = ckt.CTkLabel(master=self.show_frame,text="67-",font=("Arial",20))
    self.txt_soil_67.place(relx=0.795, rely=0.41, anchor="center")

    self.txt_soil_100 = ckt.CTkLabel(master=self.show_frame,text="100-",font=("Arial",20))
    self.txt_soil_100.place(relx=0.7915, rely=0.23, anchor="center")

    self.txt_soil_unit = ckt.CTkLabel(master=self.show_frame,text="%",font=("Arial",32))
    self.txt_soil_unit.place(relx=0.83, rely=0.23, anchor="center")

    # Illumination
    self.txt_ilu = ckt.CTkLabel(master=self.show_frame,text="Illumination",font=("Arial",20))
    self.txt_ilu.place(relx=0.94, rely=0.12, anchor="center")

    self.ilu_progress = ckt.CTkProgressBar(self.show_frame,orientation="vertical",width=20,height=180,progress_color='#99993A')
    self.ilu_progress.place(relx=0.94, rely=0.50, anchor="center")

    self.txt_ilu = ckt.CTkLabel(master=self.show_frame,text="150 lx",font=("Arial",24),bg_color='#DDDDFF',width=60,height=40,corner_radius=10)
    self.txt_ilu.place(relx=0.94, rely=0.9, anchor="center")

    self.txt_ilu_1 = ckt.CTkLabel(master=self.show_frame,text="1-",font=("Arial",20))
    self.txt_ilu_1.place(relx=0.928, rely=0.77, anchor="center")

    self.txt_ilu_10 = ckt.CTkLabel(master=self.show_frame,text="10-",font=("Arial",20))
    self.txt_ilu_10.place(relx=0.925, rely=0.59, anchor="center")

    self.txt_ilu_100 = ckt.CTkLabel(master=self.show_frame,text="100-",font=("Arial",20))
    self.txt_ilu_100.place(relx=0.9215, rely=0.41, anchor="center")

    self.txt_ilu_1000 = ckt.CTkLabel(master=self.show_frame,text="1000-",font=("Arial",20))
    self.txt_ilu_1000.place(relx=0.9180, rely=0.23, anchor="center")

    self.txt_ilu_unit = ckt.CTkLabel(master=self.show_frame,text="lx",font=("Arial",32))
    self.txt_ilu_unit.place(relx=0.96, rely=0.23, anchor="center")
