
import math as mt

def update_temp(self):
    self.temp_progress.set((self.measure_value['temp']-15)/47)
    temp = str(self.measure_value['temp'])
    if round(self.measure_value['temp'])==self.measure_value['temp']:
        temp += ".0"
    self.txt_temp.configure(text= temp + "°C")

def update_hum(self):
    self.hum_progress.set((self.measure_value['hum'])/100)
    temp = str(self.measure_value['hum'])
    if round(self.measure_value['hum'])==self.measure_value['hum']:
        temp += ".0"
    self.txt_hum.configure(text= temp + "%")

def update_soil(self):
    temp = str(self.measure_value['soil'])
    self.soil_progress.set((self.measure_value['soil'])/100)
    if round(self.measure_value['soil'])==self.measure_value['soil']:
        temp += ".0"
    self.txt_soil.configure(text= temp + "%" )

def update_ilu(self):
    self.ilu_progress.set((mt.log10(self.measure_value['ilu']))/3)
    temp = str(self.measure_value['ilu'])
    self.txt_ilu.configure(text= temp + " lx" )