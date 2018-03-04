import serial
import time
import atexit

arduino = None

def start_timer(arduino):
    arduino.write(("S\n").encode())

def stop_timer(arduino):
    arduino.write(("Z\n").encode())

def connect(port = '/dev/cu.usbserial-DN01DKJZ'):
    global arduino
    arduino = serial.Serial(port, 9600, timeout=0.5)
    time.sleep(1)
    return arduino

def disconnect(arduino):
    arduino.close()

ardunio = connect()
start_timer(arduino)
