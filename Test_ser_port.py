
import serial
import time

def delay_microseconds(microseconds):
    start_time = time.perf_counter()
    end_time = start_time + microseconds / 1_000_000
    while time.perf_counter() < end_time:
        pass

# Open serial port
uart = serial.Serial('COM3', baudrate=9600,timeout=2)  # Adjust 'COM1' and baud rate as needed
uart.bytesize = serial.EIGHTBITS
uart.stopbits = serial.STOPBITS_ONE
uart.parity = serial.PARITY_NONE


data = "Bye!"
data_bytes = [ord(char) for char in data]

# Write data to the serial port
for byte in data_bytes:
    uart.write(byte.to_bytes(1,'big'))
    delay_microseconds(200)

# Read data from the serial port
response = uart.read(100)  # Read up to 100 bytes

# Print the response
print(response)

# Close the serial port
#uart.close()

#≡print(data_bytes)






