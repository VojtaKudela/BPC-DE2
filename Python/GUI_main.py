
import customtkinter as ckt
from GUI_create import createGUI
from ilu_GUI import ilu_GUI
from soil_GUI import soil_GUI
from hum_GUI import hum_GUI
from temp_GUI import temp_GUI
from time_GUI import time_GUI
from graph_GUI import graph_GUI
from update_measure_value_func import update_temp,update_hum,update_soil,update_ilu
from data_func import default_data,full_reg_data
from raw_data import raw_data
from data_file import data_file
import time
import serial
import threading

class App(ckt.CTk):
    def __init__(self, nserial_port = "COM3", nbaud_rate=9600):
        super().__init__()
        createGUI(self)
        self.default_data()
        self.serial_port = nserial_port
        self.baud_rate = nbaud_rate
        self.running = True
        self.serial_connection = None
        raw = raw_data()
        self.data = data_file(raw)
        self.data.create_database()

    def GUI_set_temp(self):
        self.temp_win = temp_GUI(self)
        self.temp_win.mainloop()

    def GUI_set_hum(self):
        self.hum_win = hum_GUI(self)
        self.hum_win.mainloop()

    def GUI_set_soil(self):
        self.soil_win = soil_GUI(self)
        self.soil_win.mainloop()
    
    def GUI_set_ilu(self):
        self.ilu_win = ilu_GUI(self)
        self.ilu_win.mainloop()

    def GUI_connect(self):
        if (self.phase == 0):
            flat = self.start_serial()
            if (flat == 0):
                self.connect_but.configure(fg_color='#77FF77',text="Run")
                self.phase = 1
            else:
                self.connect_but.configure(fg_color='#FF7777',text="Connect")
                self.phase = 0

        elif (self.phase == 1):
            self.connect_but.configure(fg_color='#FF7777',text="Stop")
            self.phase = 2
            
        elif (self.phase == 2):
            self.stop_serial()
            self.connect_but.configure(fg_color='#DDDDDD',text="Connect")
            self.phase = 0

    def GUI_set_time(self):
        self.time_win = time_GUI(self)
        self.time_win.mainloop()

    def GUI_graph_res(self):
        self.graph_win = graph_GUI() #(self)
        self.graph_win.mainloop()

    def update_settings(self):
        temp = str(self.setting['ilu_val']) + " lx"
        self.txt_set_ilu_value.configure(text=temp)

        temp = str(self.setting['hum_val']) + " % ± " + str(self.setting['hum_hys']) + " %"
        self.txt_set_hum_value.configure(text=temp)

        temp = str(self.setting['soil_val']) + " % ± " + str(self.setting['soil_hys']) + " %"
        self.txt_set_soil_value.configure(text=temp)

        temp = str(self.setting['temp_val']) + "°C ± " + str(self.setting['temp_hys']) + "°C"
        self.txt_set_temp_value.configure(text=temp)

        self.create_reg_packet()
        self.send_reg_packet()

    def update_measure_value(self):
        update_temp(self)
        update_hum(self)
        update_soil(self)
        update_ilu(self)

    def default_data(self):
        default_data(self)
        self.update_settings()
        self.update_measure_value()

    def send_time_packet(self):
        if (self.phase == 2):
            print(self.time_packet)####
            self.send_message(self.time_packet)

    def send_reg_packet(self):
        if (self.phase == 2):
            print(self.reg_packet)####
            self.send_message(self.reg_packet)

    def create_reg_packet(self):         
        full_reg_data(self)

    def start_serial(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port,self.baud_rate,timeout=1)
            self.serial_thread = threading.Thread(target=self.read_from_serial, daemon=True)
            self.serial_thread.start()
        except serial.SerialException as e:
            #print(f"Error: {e}\n")
            return 1
        else: 
            return 0

    def read_from_serial(self):
        while self.running:
            if self.serial_connection and self.serial_connection.in_waiting > 0 and self.phase == 2:
                try:
                    line = self.serial_connection.readline()

                except Exception as e:
                    print(f"Error reading data: {e}\n")#?
                else:
                    raw = raw_data()
                    for i in range (0,13,1):
                        raw.add(line[i])
                    self.data = data_file(raw)
                    self.measure_value['ilu'] = self.data.lig
                    self.measure_value['soil'] = self.data.soil
                    self.measure_value['hum'] = self.data.hum
                    self.measure_value['temp'] = self.data.temp
                    self.update_measure_value()
                    self.data.save_data()
            time.sleep(0.1)

    def stop_serial(self):
        self.running = False
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            #print("Serial connection closed.\n")
    
    def send_message(self,message):
        if self.serial_connection and self.serial_connection.is_open:
            if message:
                try:
                    self.serial_connection.write(message)
                    print(f"Sent: {message}\n")
                except Exception as e:
                    print(f"Error sending message: {e}\n")#
            else:#
                print("No message to send.\n")#
        else:#
            print("Serial connection not open.\n")#

if __name__ == "__main__":  
    interface = App("COM3",9600)
    interface.mainloop()
