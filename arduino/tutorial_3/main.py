import serial
import time

arduino = serial.Serial('com4',9600)
time.sleep(1)

arduino.write(b'1')
arduino.close()