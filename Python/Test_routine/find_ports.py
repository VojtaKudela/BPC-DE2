import serial.tools.list_ports

def list_usb_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")

if __name__ == "__main__":
    list_usb_ports()
    print('end')
