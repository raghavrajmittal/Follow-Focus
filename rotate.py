import serial
import time
import atexit

arduino = None

def rotate(arduino, direction):
    print(direction)
    if direction > 0:
        arduino.write(("L\n").encode())

    elif direction < 0:
        arduino.write(("R\n").encode())

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
