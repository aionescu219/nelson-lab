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

ser.write(enq.encode("ascii"))
ser.read()

for x in cmd:
	ser.write(x.encode("ascii"))
	
response = ser.read()

if response == ack.encode("ascii"):
	ser.write(eot.encode("ascii")
	