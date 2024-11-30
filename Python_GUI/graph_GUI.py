"""
#############################################################
 # 
 # Class for creating a window for graphical results showing.
 # (c) 2024 Antonin Putala, MIT license
 #
 # Developed using Visual Studio Code.
 #
#############################################################
"""

"""
 # @file 
 # @defgroup putala_win class graph_GUI
 # @code import graph_GUI @endcode
 #
 # @brief Class creates a window for displaying data from the database. 
 #        The window contains a graph, a menu for selecting a quantity, 
 #        a drop-down menu for selecting a time period, and two buttons.
 # 
 # @details The window contains two buttons: Apply and Close. Pressing 
 #          the Close button closes the window. Pressing the Apply 
 #          button displays the progress taken for the selected period.
 #
 #          The variables can be selected from temperature, humidity, 
 #          soil moisture or illumination. From the time periods, you 
 #          can select the last minute, hour, day, week, month, year 
 #          or all dates.
 # 
 # @warning Chronological arrangement of data in the database is required.
 #
 # @author Antonin Putala, Dept. of Radio Electronics, Brno University 
 #         of Technology, Czechia
 # @copyright (c) 2024 Antonin Putala, This work is licensed under 
 #                the terms of the MIT license
 # @{
"""

# Imports
import customtkinter as ckt        # Custom Tkinter is used to create GUI.
from database import database      # Enable load data from text file.
import tkinter as tk               # Import intVar for RadioButton.
import matplotlib.pyplot as plt    # Import tools for graphs.
from graph_func import *           # Packet with help function for 
                                   # handeling with graph data.

                                   # Enable input graph to GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graph_GUI(ckt.CTk):
    """
# @brief   Creates a window to display graphical results.
#          Loads data from a database text file.
# @param   None
# @return  None
    """
    def __init__(self):
        super().__init__()
        self.create_GUI()
        self.data = database()

    """
# @brief   Creates GUI widgets. Set size and title 
#          of the window. Window is not resizable.
# @param   None
# @return  None
    """
    def create_GUI(self):
        self.title('Graphical results')
        self.geometry("700x400")
        self.resizable(False,False)
        self.create_graph()

    """
# @brief   Selects and edits data from a database 
#          for display in a chart.
# @param   None
# @return  None
    """
    def draw(self):
        # Reload data file from database
        self.data.load_data()
        # Filtered data from last minute, hour...
        filtered_data = []
        # Display data od X axis
        x_data = []
        # Display data od Y axis
        y_data = []
        # Pointer in database
        i = -1
        # Sets the selected time period.
        match (self.time_scale.get()):
            case "Last minute":
                # The data was taken in the last minute, if neither the minute nor the hour changed...
                while ((int(self.data.data[-1]["min"]) == int(self.data.data[i]["min"])) & 
                                        (int(self.data.data[-1]["hour"]) == int(self.data.data[i]["hour"])) &
                                        (int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])
                    # Stores data for the x-axis. The data is in seconds.
                    x_data.append(int(self.data.data[i]["sec"]))
                    # Next step
                    i -= 1

            # The data was taken in the last hour, if neither the hour nor the day changed...
            case "Last hour":
                while ((int(self.data.data[-1]["hour"]) == int(self.data.data[i]["hour"])) & 
                                        (int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])
                    # Stores data for the x-axis. The data is in minutes. The seconds are divided by 60.
                    x_data.append(int(self.data.data[i]["min"])+int(self.data.data[i]["sec"])/60)
                    # Next step
                    i -= 1

            case "Last day":
            # The data was taken in the last day, if neither the date nor the month changed...
                while ((int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) &
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])
                    # Stores data for the x-axis. The data is in hours. The minutes are divided by 60.
                    # The seconds are divided by 3600.
                    x_data.append(int(self.data.data[i]["hour"])+int(self.data.data[i]["min"])/60 +
                                    int(self.data.data[i]["sec"])/3600)
                    # Next step                    
                    i -= 1

            case "Last week":
            # A separate function indicates whether a day is in a specific week.
                while (self.week_con(i)):
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])

                    # If the week ends at the turn of the month.
                    if (int(self.data.data[-1]["month"])) != int(self.data.data[i]["month"]):
                        # Days from the previous month have a negative value.
                        days = int(self.data.data[i]["date"]) - n_of_days(self.data.data[i]["month"],self.data.data[i]["year"])
                    else:
                        # The number of days is simply a date.
                        days = int(self.data.data[i]["date"])

                    # Stores data for the x-axis. The data is in dayes. The hours are divided by 24.
                    # The minutes are divided by 1440. The seconds are divided by 86400.
                    x_data.append(days+int(self.data.data[i]["hour"])/24+
                                    int(self.data.data[i]["min"])/1440+int(self.data.data[i]["sec"])/86400)
                    # Next step                    
                    i -= 1

            case "Last month":
            # The data was taken in the last month, if neither the month nor the year changed...
                while ((int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                    (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                    (abs(i) < len(self.data.data))):
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])
                    # Stores data for the x-axis. The data is in dayes. The hours are divided by 24.
                    # The minutes are divided by 1440. The seconds are divided by 86400.
                    x_data.append(int(self.data.data[i]["date"])+int(self.data.data[i]["hour"])/24+
                                    int(self.data.data[i]["min"])/1440+int(self.data.data[i]["sec"])/86400)
                    # Next step
                    i -= 1

            case "Last year":
            # The data was taken in the last year, if the year was not changed...
                while ((int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                       (abs(i) < len(self.data.data))):
                    # The number of days in a given month.
                    days = n_of_days(self.data.data[i]["month"],self.data.data[i]["year"])
                    # The selected data is filtered.
                    filtered_data.append(self.data.data[i])

                    # Stores data for the x-axis. The data is in months. The hours are divided by 24.
                    # The minutes are divided by 1440. The seconds are divided by 86400.
                    # The sum of dates less than a month is divided by the number of days in that month.
                    x_data.append(int(self.data.data[i]["month"])+(int(self.data.data[i]["date"])+
                                    int(self.data.data[i]["hour"])/24+int(self.data.data[i]["min"])/1440+
                                    int(self.data.data[i]["sec"])/86400)/days)
                    # Next step
                    i -= 1

            case _:
            # All data are processed.
                for i in range(-1,-len(self.data.data)-1,-1):
                    # The number of days that have passed until the beginning of the given month.
                    days = n_of_days_cum(self.data.data[i]["month"],self.data.data[i]["year"])
                    # Number of days in the year.
                    y_days = n_of_days_year(self.data.data[i]["year"])

                    # Stores data for the x-axis. The data is in years. The hours are divided by 24.
                    # The minutes are divided by 1440. The seconds are divided by 86400.
                    # The date and the number of days until the beginning of the month are added to these 
                    # values. This figure is divided by the number of days in the year and 
                    # the year is added to it.
                    x_data.append(int(self.data.data[i]["year"])+((days+
                                    int(self.data.data[i]["date"])+(int(self.data.data[i]["hour"])/24)+
                                    (int(self.data.data[i]["min"])/1440)+(int(self.data.data[i]["sec"])/86400))/y_days))
                    # Selects everything. Here, only the list rotation takes place.
                    filtered_data.append(self.data.data[i])
 
        # From the filtered rows, only the values ​​of the quantity that will be 
        # on the vertical axis are selected.
        for i in range(0,len(filtered_data),1):
            # Determination of the selected quantity.
            match (self.radio_var.get()):
                case 1:
                    y_data.append(float(filtered_data[i]["temp"]))
                case 2:
                    y_data.append(float(filtered_data[i]["hum"]))
                case 3:
                    y_data.append(float(filtered_data[i]["soil"]))
                case _:
                    y_data.append(float(filtered_data[i]["lig"]))
        
        # The loaded data is displayed in a graph.
        self.update_graph(x_data,y_data)

    """
# @brief   Creates GUI widgets and axes.
# @param   None
# @return  None
# @details The window contains axes, 
#          two buttons Draw and Close, selection 
#          of quantities and setting of the time 
#          period using the drop-down menu.
    """
    def create_graph(self):
        """Creates axes in the window and places them in the right part of the window."""
        self.fig,self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0,rely=0.5,anchor='w')
        
        """
        Creates a radio button menu for selecting a variable. It is 
        possible to select temperature, humidity, soil moisture or illumination.
        """
        self.radio_var = tk.IntVar(value=1)
        self.radio_temp = ckt.CTkRadioButton(self, text="Temperature",
                                            variable = self.radio_var, value = 1)
        self.radio_temp.place(relx=0.8,rely=0.1)
        self.radio_hum = ckt.CTkRadioButton(self, text="Humidity",
                                            variable = self.radio_var, value = 2)
        self.radio_hum.place(relx=0.8,rely=0.2)
        self.radio_soil = ckt.CTkRadioButton(self, text="Soil moisure",
                                            variable = self.radio_var, value = 3)
        self.radio_soil.place(relx=0.8,rely=0.3)
        self.radio_ilu = ckt.CTkRadioButton(self, text="Illumination",
                                            variable = self.radio_var, value = 4)
        self.radio_ilu.place(relx=0.8,rely=0.4)

        """ Create Close button. Press to destroy window."""
        self.but_close = ckt.CTkButton(self,text="Close",command=self.destroy,width=150,height=40,
                                       font=('Arial',20))
        self.but_close.place(relx=0.76,rely=0.85)

        """ Create Draw button. It has callback function self.draw."""
        self.but_draw = ckt.CTkButton(self,text="Draw",command=self.draw,width=150,height=40,
                                      font=('Arial',20))
        self.but_draw.place(relx=0.76,rely=0.7)

        """
        Creates a drop-down menu for selecting a time period. You can select
        the last minute, hour, day, week, month, year, or all dates.
        """
        self.time_scale = ckt.CTkComboBox(master=self,width=150,font=('Arial',20),state='readonly',
                                          values=['Last minute','Last hour','Last day','Last week',
                                                  'Last month','Last year','All'])
        # Default value
        self.time_scale.set("All")
        self.time_scale.place(relx=0.76,rely=0.56,anchor='w') 

    """
# @brief   Displays new data in the graph.
# @param   x_data x-coordinates of points
# @param   y_data y-coordinates of points
# @return  None
# @details Deletes previous graph data. 
#          Displays new data. Changes the 
#          vertical and horizontal axis labels.
    """
    def update_graph(self,x_data,y_data):
        # Deletes previous graph data.
        self.ax.cla()
        # Displays new data.
        self.ax.plot(x_data,y_data)
        # Changes the horizontal axis labels.
        set_xlabel(self)
        # Changes the vertical axis labels. 
        set_ylabel(self)
        # Displays changes.
        self.canvas.draw() 

    """
# @brief   It verifies whether the given day 
#          was or was not during the last week.
# @param   i (int) The order of the line being read.
# @return  Was it within the last month.
# @note    It also checks the situation when 
#          last week is at the turn of the month 
#          or even the turn of the year.
    """
    def week_con(self,i):
        # Same month
        a1 = (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"]))
        a2 = (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"]))
        a3 = (int(self.data.data[-1]["date"]) - int(self.data.data[i]["date"]) < 7)
        a4 = (int(self.data.data[-1]["date"]) - int(self.data.data[i]["date"]) >= 0)
        a = a1 & a2 & a3 & a4
        # Consecutive months
        b1 = (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"]))
        b2 = (int(self.data.data[-1]["month"]) - int(self.data.data[i]["month"]) == 1)
        b3 = (int(self.data.data[-1]["date"]) + n_of_days(self.data.data[i]["month"],self.data.data[i]["year"]) - 
              int(self.data.data[i]["date"]) < 7)
        b = b1 & b2 & b3
        # Consecutive months, consecutive years
        c1 = (int(self.data.data[-1]["year"]) - int(self.data.data[i]["year"]) == 1)
        c2 = (int(self.data.data[-1]["month"]) == 1)
        c3 = (int(self.data.data[i]["month"]) == 12)
        c4 = (int(self.data.data[-1]["date"]) + 31 - int(self.data.data[i]["date"]) < 7)
        c = c1 & c2 & c3 & c4
        # The last condition is if all data is from last week.
        return (a | b | c) & (abs(i) < len(self.data.data))
    
"""&}"""