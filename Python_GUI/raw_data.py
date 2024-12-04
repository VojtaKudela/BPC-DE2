"""
#############################################################
 # 
 # Class for saving received UART data.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""
##
# @file 
# @defgroup putala_data Data classes
# @code import raw_data @endcode
#
# @brief Class raw_ data is intended as a buffer for data received from UART
#
# Class enables to add elements and show storage data in different number systems
#
# @author Antonin Putala, Dept. of Radio Electronics, Brno University 
#         of Technology, Czechia
# @copyright (c) 2024 Antonin Putala, This work is licensed under 
#                the terms of the MIT license
# @{


class raw_data:

    def __init__(self):
        """!
        @brief   Create buffer for receive UART data.
        @param   None
        @return  None
        @details Create in object raw_data empty list.
        """
        self.list = []


    def add(self,data):
        """!
        @brief   Add new byte to the buffer.
        @param   data New byte, which have to be stogare
        @return  None
        @details New byte will be storage in list.
        """
        self.list.append(data)


    def show_bin(self):
        """!
        @brief   Display list value binary in the console.
        @param   None
        return   None
        @note    Only for debuging.
        """
        string = 'Binary values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]:b} '
        print(string)


    def show_hex(self):
        """!
        @brief   Display list value hexadecimally in the console.
        @param   None
        return   None
        @note    Only for debuging.
        """
        string = 'Hexadecimal values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]:x} '
        print(string)


    def show_dec(self):
        """!
        @brief   Display list value binary in the console.
        @param   None
        return   None
        @note    Only for debuging.
        """
        string = 'Decimal values: '
        for i in range(0,len(self.list),1):
            string += f'{self.list[i]} '
        print(string)

##@}