import serial
import time
import atexit

arduino = None

def start_timer(arduino):
    print("hola")
    arduino.write(("S\n").encode())

def stop_timer(arduino):
    print("hey")
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
