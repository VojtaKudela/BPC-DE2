
# Import widgets for GUI
import customtkinter as ckt
# Enable load data from text file
from database import database
# Import intVar for RadioButton
import tkinter as tk
# Import tools for graphs
import matplotlib.pyplot as plt
# Packet with help function for handeling with graph data
from graph_func import n_of_days, n_of_days_year, n_of_days_cum, set_xlabel, set_ylabel
# Enable input graph to GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graph_GUI(ckt.CTk):
    def __init__(self):
        super().__init__()
        self.create_GUI()
        self.data = database()

    def create_GUI(self):
        self.title('Graphical results')
        self.geometry("700x400")
        self.resizable(False,False)
        self.create_graph()

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
        match (self.time_scale.get()):
            case "Last minute":
                while ((int(self.data.data[-1]["min"]) == int(self.data.data[i]["min"])) & 
                                        (int(self.data.data[-1]["hour"]) == int(self.data.data[i]["hour"])) &
                                        (int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    filtered_data.append(self.data.data[i])
                    x_data.append(int(self.data.data[i]["sec"]))
                    i -= 1
            case "Last hour":
                while ((int(self.data.data[-1]["hour"]) == int(self.data.data[i]["hour"])) & 
                                        (int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    filtered_data.append(self.data.data[i])
                    x_data.append(int(self.data.data[i]["min"])+int(self.data.data[i]["sec"])/60)
                    i -= 1
            case "Last day":
                while ((int(self.data.data[-1]["date"]) == int(self.data.data[i]["date"])) & 
                                        (int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) &
                                        (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                        (abs(i) < len(self.data.data))):
                    filtered_data.append(self.data.data[i])
                    x_data.append(int(self.data.data[i]["hour"])+int(self.data.data[i]["min"])/60 +
                                    int(self.data.data[i]["sec"])/3600)
                    i -= 1
            case "Last week":
                while (self.week_con(i)):
                    
                    filtered_data.append(self.data.data[i])

                    if (int(self.data.data[-1]["month"])) != int(self.data.data[i]["month"]):
                        days = int(self.data.data[i]["date"]) - n_of_days(self.data.data[i]["month"],self.data.data[i]["year"])
                    else:
                        days = int(self.data.data[i]["date"])

                    x_data.append(days+int(self.data.data[i]["hour"])/24+
                                    int(self.data.data[i]["min"])/1440+int(self.data.data[i]["sec"])/86400)
                    i -= 1

            case "Last month":
                while ((int(self.data.data[-1]["month"]) == int(self.data.data[i]["month"])) & 
                                    (int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                                    (abs(i) < len(self.data.data))):
                    filtered_data.append(self.data.data[i])
                    x_data.append(int(self.data.data[i]["date"])+int(self.data.data[i]["hour"])/24+
                                    int(self.data.data[i]["min"])/1440+int(self.data.data[i]["sec"])/86400)
                    i -= 1

            case "Last year":
                while ((int(self.data.data[-1]["year"]) == int(self.data.data[i]["year"])) & 
                       (abs(i) < len(self.data.data))):
                    days = n_of_days(self.data.data[i]["month"],self.data.data[i]["year"])
                    filtered_data.append(self.data.data[i])
                    x_data.append(int(self.data.data[i]["month"])+(int(self.data.data[i]["date"])+
                                    int(self.data.data[i]["hour"])/24+int(self.data.data[i]["min"])/1440+
                                    int(self.data.data[i]["sec"])/86400)/days)
                    i -= 1

            case _:
                for i in range(-1,-len(self.data.data)-1,-1):
                    days = n_of_days_cum(self.data.data[i]["month"],self.data.data[i]["year"])
                    y_days = n_of_days_year(self.data.data[i]["year"])
                    x_data.append(int(self.data.data[i]["year"])+((days+
                                    int(self.data.data[i]["date"])+(int(self.data.data[i]["hour"])/24)+
                                    (int(self.data.data[i]["min"])/1440)+(int(self.data.data[i]["sec"])/86400))/y_days))
                    filtered_data.append(self.data.data[i])
 
        for i in range(0,len(filtered_data),1):
            match (self.radio_var.get()):
                case 1:
                    y_data.append(float(filtered_data[i]["temp"]))
                case 2:
                    y_data.append(float(filtered_data[i]["hum"]))
                case 3:
                    y_data.append(float(filtered_data[i]["soil"]))
                case _:
                    y_data.append(float(filtered_data[i]["lig"]))
        
        self.update_graph(x_data,y_data)

    def create_graph(self):
        self.fig,self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(relx=0,rely=0.5,anchor='w')
        
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

        self.but_close = ckt.CTkButton(self,text="Close",command=self.destroy,width=150,height=40,font=('Arial',20))
        self.but_close.place(relx=0.76,rely=0.85)

        self.but_draw = ckt.CTkButton(self,text="Draw",command=self.draw,width=150,height=40,font=('Arial',20))
        self.but_draw.place(relx=0.76,rely=0.7)

        self.time_scale = ckt.CTkComboBox(master=self,width=150,font=('Arial',20),state='readonly',values=['Last minute','Last hour','Last day','Last week','Last month','Last year','All'])
        self.time_scale.set("All")
        self.time_scale.place(relx=0.76,rely=0.56,anchor='w') 

    def update_graph(self,x_data,y_data):
        self.ax.cla()
        self.ax.plot(x_data,y_data)
        set_xlabel(self)
        set_ylabel(self)
        self.canvas.draw() 

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
        return (a | b | c)

#if __name__ == "__main__":  
#    win = graph_GUI()
#    win.mainloop()
