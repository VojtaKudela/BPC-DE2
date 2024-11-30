"""
#############################################################
 # 
 # Class for processing received UART data.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_data class data_file
 # @code import data_file @endcode
 #
 # @brief Class intended to processing data received from UART.
 #
 # Received UART data are decoded and storage in dictionary to
 # the element with the appropriate name.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

from num_and_days import num2day, day2num

class data_file:
    """
# @brief   Create dictionary. Dictionary is fulled
#          using object raw_data.
# @param   raw_data Object which contains data received from UART.
# @return  None
    """
    def __init__(self,raw_data):
        self.set_default()
        self.upgrade_data(raw_data)

    """
# @brief   Create dictionary. Dictionary is fulled
#          with default data.
# @param   None
# @return  None
    """   
    def set_default(self):
        self.soil = 0
        self.lig = 0
        self.temp = 0
        self.hum = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.day = 'Su'
        self.date = 0
        self.month = 0
        self.year = 0    

    """
# @brief   Import data from raw_data to dictionary.
# @param   raw_data Object which contains data received from UART.
# @return  None
    """ 
    def upgrade_data(self,raw_data):
        data = raw_data.list
        self.soil = self.get_soil(data)
        self.lig  = self.get_lig(data)
        self.temp = self.get_temp(data)
        self.hum = self.get_hum(data)
        self.sec = self.get_sec(data)
        self.min = self.get_min(data)
        self.hour = self.get_hour(data)
        self.day = self.get_day(data)
        self.date = self.get_date(data)
        self.month = self.get_month(data)
        self.year = self.get_year(data)

    """
# @brief   Decode soil moisure data.
# @param   raw_data Object which contains data received from UART.
# @return  Measured value of soil moisure.
    """        
    # Modify function to get meaningful value
    def get_soil(self,raw_data):
        if (len(raw_data)>0):
            return raw_data[-1]

    """
# @brief   Decode illumination data.
# @param   raw_data Object which contains data received from UART.
# @return  Measured value of illumination.
    """          
    # Modify function to get meaningful value
    def get_lig(self,raw_data):
        if (len(raw_data)>1):
            return raw_data[-2]

    """
# @brief   Decode temperature data.
# @param   raw_data Object which contains data received from UART.
# @return  Measured value of temperature.
    """           
    def get_temp(self,raw_data):
        if (len(raw_data)>3):
            return raw_data[-4]+raw_data[-3]*0.1
            # (raw_data[-4]>>4)*10+(raw_data[-4]&15)+raw_data[-3]*0.1

    """
# @brief   Decode humidity data.
# @param   raw_data Object which contains data received from UART.
# @return  Measured value of humidity.
    """
    def get_hum(self,raw_data):
        if (len(raw_data)>5):
            return raw_data[-6]+raw_data[-5]*0.1 
            # (raw_data[-6]>>4)*10+(raw_data[-6]&15)+raw_data[-5]*0.1

    """
# @brief   Decode information about time; seconds.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; seconds.
    """        
    def get_sec(self,raw_data):
        if (len(raw_data)>6):
            return (raw_data[-7]>>4)*10+(raw_data[-7]&15)

    """
# @brief   Decode information about time; minutes.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; minutes.
    """               
    def get_min(self,raw_data):
        if (len(raw_data)>7):
            return (raw_data[-8]>>4)*10+(raw_data[-8]&15)

    """
# @brief   Decode information about time; hours.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; hours.
    """         
    def get_hour(self,raw_data):
        if (len(raw_data)>8):
            return ((raw_data[-9]>>5)&1)*20+((raw_data[-9]>>4)&1)*10+(raw_data[-9]&15)

    """
# @brief   Decode information about time; days in the week.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; days.
# @retval  Su, Mo, Tu, We, Th, Fr, Sa, Su.
    """        
    def get_day(self,raw_data):
        if (len(raw_data)>9):
            return num2day(raw_data[-10])

    """
# @brief   Decode information about time; date.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; date.
    """         
    def get_date(self,raw_data):
        if (len(raw_data)>10):
            return (raw_data[-11]>>4)*10+(raw_data[-11]&15)

    """
# @brief   Decode information about time; months.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; month. Order of the month.
    """            
    def get_month(self,raw_data):
        if (len(raw_data)>11):
            return ((raw_data[-12]>>4)&1)*10+(raw_data[-12]&15)

    """
# @brief   Decode information about time; years.
# @param   raw_data Object which contains data received from UART.
# @return  Time value; year.
    """           
    def get_year(self,raw_data):
        if (len(raw_data)>12):
            return (raw_data[-13]>>4)*10+(raw_data[-13]&15)+1900+(raw_data[-12]>>7)*100

    """
# @brief   Display storage data in the console.
# @param   None
# @return  None
# @note    Only for debuging.
    """          
    def show_data(self):
        print(f'{self.year}-{self.month}-{self.date} {self.day} {self.hour}:{self.min}:{self.sec} - {self.temp}°C, {self.hum} %, {self.lig} lx, {self.soil} %')

    """
# @brief   Create or open file to storage measured data.
# @param   None
# @return  None
# @warning For futher processing of data, it is necessary
#          that the data follow chronologically. 
#          Please delete data with the wrong time.
    """ 
    def create_database(self):
        try:
            f = open("database.txt","a")
        except:
            f = open("database.txt","w")
            f.write(f'Year\tMo\tDa\tDy\tHour\tMin\tSec\tTemp\tHuma\tLig\tSoil\t')
        finally:
            f.close()

    """
# @brief   Save measured data to text file.
# @param   None
# @return  None
# @details Data are saving to a line in this format:
#          year-month-date-day-hour-minute-second
#          -temperature-humidity-illumination-soil moisure.
    """ 
    def save_data(self):
        f = open("database.txt","a")
        f.write(f'\n{self.year}\t{self.month}\t{self.date}\t{self.day}\t{self.hour}\t{self.min}\t{self.sec}\t{self.temp}\t{self.hum}\t{self.lig}\t{self.soil}\t')
        f.close()

"""@}"""