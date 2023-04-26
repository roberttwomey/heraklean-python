import serial

# python:
def feedPaperCut():
	ser.write([27, 100, 8]) # feed
	ser.write([27, 105]) # cut

def linefeed():
	ser.write(b'\n')

ser = serial.Serial('/dev/tty.usbserial-110', 4800, 8, 'N', rtscts=1)  # open serial port
print(ser.name)         # check which port was really used
ser.write(bytearray([27, 114, 1])) # selects color 1
ser.write(b'hello'+b'\n')     # write a string
ser.write(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'+b'\n')
linefeed()
linefeed()
ser.write(b'----\n')
feedPaperCut()
ser.close()             # close port

# // feed paper and cut
# ~printer.putAll([27, 100, 8]);
# ~printer.putAll([27, 105]);

			
# port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)


# supercollider:
# ~printer = SerialPort(printerport, 4800, 8, true, nil, true);
# SerialPort.new(port, baudrate: 9600, databits: 8, stopbit: true, parity, crtscts: false, xonxoff: false, exclusive: false)

# port	
# A String representing the port to be opened. (An Integer index into *devices is allowed, but this is deprecated.)

# baudrate	
# Integer baud rate, typically in the range [4800..230400].

# databits	
# Bits per character. Typically 8, but can be any integer.

# stopbit	
# A Boolean indicating whether to use two stop bits (true) or one stop bit (false).

# parity	
# Whether the port uses even, odd, or no parity. Pass 'even', 'odd', or nil (for none).

# crtscts	
# A Boolean indicating whether to use hardware flow control (RTS/CTS signals).