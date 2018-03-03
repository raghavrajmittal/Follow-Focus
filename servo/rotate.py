import serial
import time

# def connect(port):
#     # close()
#     global arduino
#     arduino = serial.Serial(port, 9600)

def rotate(arduino, direction, angle):

    time.sleep(1)
    arduino.write(direction + str(angle))

def connect(port = '/dev/cu.usbserial-DN01DQRE'):
    arduino = serial.Serial(port, 9600)
    return arduino

def disconnect(arduino):
    arduino.close()


# close()
