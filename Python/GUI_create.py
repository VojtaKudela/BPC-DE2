
from createGUIshow import createGUIshow
from createGUIset import createGUIset
import customtkinter as ckt
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

def createGUI(self):
    createGUIshow(self)
    createGUIset(self)

    self.connect_but = ckt.CTkButton(master=self,text="Connect",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_connect)
    self.connect_but.place(relx=0.18, rely=0.1, anchor="center")

    self.set_time_but = ckt.CTkButton(master=self,text="Set time",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_set_time)
    self.set_time_but.place(relx=0.18, rely=0.2, anchor="center")

    self.set_graph_but = ckt.CTkButton(master=self,text="Graphical results",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_graph_res)
    self.set_graph_but.place(relx=0.18, rely=0.3, anchor="center")

    #fig = plt.Figure(figsize = (7, 5),dpi = 100)
    #x = np.linspace(0,2*np.pi,101)
    #y = np.sin(x)
    #plot1 = fig.add_subplot(111)  
    #plot1.plot(x,y)

    #self.canvas = FigureCanvasTkAgg(fig, master = self)   
    #self.canvas.draw()
    #self.canvas.get_tk_widget().pack(side=tk.RIGHT) 

    #menu_graph = ckt.CTkComboBox(self, values=["Temperature", "Humidity","Illumination","Soil moisture"])
    #menu_graph.set("Temperature")
    #menu_graph.place(relx=0.26, rely=0.9, anchor="center")

    
    
    #self.my_buttom = ckt.CTkButton(master=self.my_frame,width=100,height=50)
    #self.my_buttom.place(relx=0.5, rely=0.7, anchor="center")

    
    