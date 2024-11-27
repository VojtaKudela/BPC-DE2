
from createGUIshow import createGUIshow
from createGUIset import createGUIset
import customtkinter as ckt
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np

def createGUI(self):
    self.title("Tropical plants")
    self.resizable(False, False) 
    self.geometry("800x500")
    
    createGUIshow(self)
    createGUIset(self)

    self.connect_but = ckt.CTkButton(master=self,text="Connect",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_connect)
    self.connect_but.place(relx=0.18, rely=0.1, anchor="center")

    self.set_time_but = ckt.CTkButton(master=self,text="Set time",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_set_time)
    self.set_time_but.place(relx=0.18, rely=0.2, anchor="center")

    self.set_graph_but = ckt.CTkButton(master=self,text="Graphical results",font=("Arial",24),width=200,height=25,fg_color='#DDDDDD',text_color='#444444',command=self.GUI_graph_res)
    self.set_graph_but.place(relx=0.18, rely=0.3, anchor="center")

    
    