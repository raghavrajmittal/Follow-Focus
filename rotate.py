import serial
import time
import atexit

arduino = None

def rotate(arduino, angle):
    if len(angle) == 2:
        angle = str(angle[0]) + "0" + str(angle[1])

    if "00" in angle:
        return

    print("writing:", angle)
    arduino.write((str(angle)+"\n").encode())

def connect(port = '/dev/cu.usbserial-DN01DQRE'):
    global arduino
    arduino = serial.Serial(port, 9600, timeout=0.5)
    time.sleep(1)
    return arduino

def disconnect(arduino):
    arduino.close()

# def exit_handler():
#     global arduino
#
#     if arduino:
#         disconnect(arduino)
#
# atexit.register(exit_handler)
#
# pi = connect()
# while True:
#
#     rotate(pi, "R50")
#     time.sleep(2.0)
#     rotate(pi, "L50")
#     time.sleep(2.0)
