import serial
import time

# python:
def feedPaperCut():
	ser.write([27, 100, 8]) # feed
	ser.write([27, 105]) # cut

def linefeed():
	ser.write(b'\n')


ser = serial.Serial('/dev/tty.usbserial-110', 4800, 8, 'N', rtscts=1)  # open serial port
print("printer opened on: ",ser.name)         # check which port was really used
ser.write(bytearray([27, 114, 1])) # selects color 1

# open file and print contents
f = open("offboarding_draft_30.txt", "r")
for line in f.readlines(): 
	print(line, end="")
	# ser.write(bytearray(line,encoding='ASCII'))
	ser.write(line.encode('ascii'))
	time.sleep(0.05)

ser.write(b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'+b'\n')

feedPaperCut()
ser.close() 

exit()