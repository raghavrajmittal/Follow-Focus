import speech_recognition as sr
import serial
import time


arduino = None
# Record Audio
r = sr.Recognizer()

# Speech recognition using Google Speech Recognition
arduino = serial.Serial('/dev/cu.usbserial-DN01DKJZ', 9600, timeout=0.5)

try:
    while True:
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            # print("You said: " + r.recognize_google(audio))
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)

            command = r.recognize_google(audio)
            
            print(command)
            if 'start' in command:
                print("in here")
                arduino.write(("S\n").encode())
            elif 'stop' in command:
                arduino.write(("X\n").encode())

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

except Exception:
    traceback.print_exc()
    print("closing connection")
    if arduino:
        arduino.close()
