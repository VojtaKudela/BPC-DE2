"""
#############################################################
 # 
 # Class for loading data from database.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

##
# @file 
# @defgroup putala_data Data classes
# @code import database @endcode
#
# @brief The class database ensures data is loaded from the database.
#        Data storage in database are loaded and saved in list of 
#        dictionary.
#
# @details One dictionary corresponds to one row. Each element 
#          carries information about time, temperature, humidity, 
#          soil moisture, or lighting.
#
# @{

class database:

    def __init__(self):
        """!
        @brief   Create empty list for saving data.
        @param   None
        @return  None
        """
        self.data = []


    def load_data(self):
        """!
        @brief   It ensures that data is read from a text file.
        @param   None
        @return  None
        """
        # Data has to be cleared. Otherwise there would be duplication.
        self.data = []
        # Open database.
        f = open("database.txt","r")
        # Get data from text file.
        lines = f.readlines()
        
        # Data from all lines are read and separated to appropriate elements.
        for i in range(1,len(lines),1):
            # One line is selected. The values are separated by tabs.
            line = lines[i].split("\t")
            # Result of this operation is list of dictionary.
            self.data.append({"year":line[0],"month":line[1],"date":line[2],
                              "day":line[3],"hour":line[4],"min":line[5],
                              "sec":line[6],"temp":line[7],"hum":line[8],
                              "lig":line[9],"soil":line[10]})
        
        # Close database.
        f.close()

##@}