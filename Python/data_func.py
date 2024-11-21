
def default_data(self):
    self.setting = {'temp_val':25,'temp_hys':2,'hum_val':50,'hum_hys':5,
                    'soil_val':50,'soil_hys':5,'ilu_val':100}
    self.system_setting = {'ilu_min':20,'ilu_max':500,'temp_val_min':15,
                            'temp_val_max':50,'temp_hys_min':1,'temp_hys_max':10,
                            'hum_val_min':20,'hum_val_max':90,'hum_hys_min':5,'hum_hys_max':30,
                            'soil_val_min':5,'soil_val_max':90,'soil_hys_min':5,'soil_hys_max':30}
    self.measure_value = {'temp':20,'hum':65.7,'soil':54,'ilu':200}
    self.time_packet = [0x54,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    self.reg_packet = [0x52,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    self.phase = 0

def full_reg_data(self):
    # Full reg packet with data
    self.reg_packet[1] = self.setting['temp_val']
    self.reg_packet[2] = self.setting['temp_hys']
    self.reg_packet[3] = self.setting['hum_val']
    self.reg_packet[4] = self.setting['hum_hys']
    self.reg_packet[5] = self.setting['soil_val']
    self.reg_packet[6] = self.setting['soil_hys']
    self.reg_packet[7] = self.setting['ilu_val']//100
    self.reg_packet[8] = self.setting['ilu_val']%100