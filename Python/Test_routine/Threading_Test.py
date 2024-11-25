import tkinter as tk
from tkinter import scrolledtext
import serial
import threading
import time

class SerialGUI:
    def __init__(self, root, serial_port="COM3", baud_rate=9600):
        self.root = root
        self.serial_port = serial_port
        self.baud_rate = baud_rate
        self.running = True
        self.serial_connection = None

        # Setup GUI
        self.root.title("Serial Port Data Viewer")
        
        self.text_area = scrolledtext.ScrolledText(root, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_serial)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_serial)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_program)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def start_serial(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            self.text_area.insert(tk.END, f"Connected to {self.serial_port} at {self.baud_rate} baud.\n")
            self.serial_thread = threading.Thread(target=self.read_from_serial, daemon=True)
            self.serial_thread.start()
        except serial.SerialException as e:
            self.text_area.insert(tk.END, f"Error: {e}\n")

    def read_from_serial(self):
        while self.running:
            if self.serial_connection and self.serial_connection.in_waiting > 0:
                try:
                    line = self.serial_connection.readline().decode('ascii').strip()
                    self.text_area.insert(tk.END, line + "\n")
                    self.text_area.yview(tk.END)  # Scroll to the end
                except Exception as e:
                    self.text_area.insert(tk.END, f"Error reading data: {e}\n")
            time.sleep(0.1)

    def stop_serial(self):
        self.running = False
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            self.text_area.insert(tk.END, "Serial connection closed.\n")

    def exit_program(self):
        self.stop_serial()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = SerialGUI(root, serial_port="COM3", baud_rate=9600)  # Change COM3 to your port
    root.mainloop()
