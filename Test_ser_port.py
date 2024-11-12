
import serial as s

# Open serial port
uart_data = s.Serial('/dev/ttyUSB2', 115200, timeout=1)  # Adjust 'COM1' and baud rate as needed

# Write data to the serial port
uart_data.write(b'Hello!')

# Read data from the serial port
response = uart_data.read(100)  # Read up to 100 bytes

# Print the response
print(response)

# Close the serial port
uart_data.close()






