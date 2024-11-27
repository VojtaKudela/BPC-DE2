from GUI_main import App

if __name__ == "__main__":  
    interface = App("COM3",9600)
    interface.mainloop()