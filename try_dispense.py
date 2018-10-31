# Activates dispense function - written to determine how to communicate with ML-808GX dispenser across 9-pin RS232

import serial
 
port = "COM5"
baud = 19200
bytesize = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE
timeout = 5
xonxoff = False
rtscts = False
dsrdtr = False

ser = serial.Serial(port, baud, bytesize, parity, stopbits, timeout, xonxoff, rtscts, dsrdtr)
    # open the serial port
  
if ser.isOpen():
     print(ser.name + ' is open...')
 
enq = 5
eot = 4
ack = 6
cmd = [2,48,52,68,73,32,32,67,70,3]

ser.write(chr(enq).encode("ascii"))
print(ser.read())

for x in cmd:
    ser.write(chr(x).encode("ascii"))
    
response = ser.read()
print("response is", response)

ser.write(chr(eot).encode("ascii"))
ser.close()
print("fin")
