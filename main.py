import serial

with serial.Serial('COM3', 9600) as ser:
    # Write data
    ser.write(b'Hello Python\n')
    # Read data
    line = ser.readline()
    print(line)
