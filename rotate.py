import serial
import time

# def connect(port):
#     # close()
#     global arduino
#     arduino = serial.Serial(port, 9600)

def rotate(arduino, angle):
    print(angle)
    #time.sleep(1)
    
    if len(angle) == 2:
        angle = str(angle[0]) + "0" + str(angle[1])

    if "00" in angle:
        return

    arduino.write(str(angle).encode())

def connect(port = '/dev/cu.usbserial-DN01DQRE'):
    arduino = serial.Serial(port, 9600)
    return arduino

def disconnect(arduino):
    arduino.close()


# close()
