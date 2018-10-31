import serial;

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM5'
#ser.open()
print(ser.is_open)
ser.write(5)
#print(ser.read(1))
