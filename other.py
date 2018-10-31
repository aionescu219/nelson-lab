import serial

 
port = "COM5"
baud = 19200
bytesize = serial.EIGHTBITS
parity = serial.PARITY_NONE
stopbits = serial.STOPBITS_ONE
timeout = 5
xonxoff = False
rtscts = False
dsrdtr = True
 
ser = serial.Serial(port, baud, bytesize, parity, stopbits, timeout, xonxoff, rtscts, dsrdtr)
    # open the serial port
if ser.isOpen():
     print(ser.name + ' is open...')
 
while True:
    cmd = input("Enter command or 'exit':")

    if cmd == 'exit':
        ser.close()
        exit()
    else:
        #print(cmd.encode('ascii'))
        #print(int(float(cmd)).encode("ascii"))
        
        ser.write(cmd.encode('ascii'))
        #ser.write(int(float(cmd)))
        out = ser.read(size=1)
        print('Receiving...'+out.decode("ascii"))