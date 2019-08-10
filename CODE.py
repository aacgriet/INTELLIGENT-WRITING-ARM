Part 1 (speech recognition) :
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
audio=r.listen(source)
try:
    print("system predicts:"+r.recognize_google(audio))
except Exception:
     print("some thing went wrong")
for i in (r.recognize_google(audio)):
      print(i)
All the above program is for converting the recorded speech to   text so that the letters will be individually printed for getting executed.
Part 2  (motion of rollers) :
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
def horfar1():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    sleep(2)
    GPIO.output(16,GPIO.LOW)
def horfar2():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(18,GPIO.LOW)
    sleep(0.25)
    GPIO.output(16,GPIO.LOW)
def verfar1():
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(38,GPIO.LOW)
    sleep(0.5)
    GPIO.output(36,GPIO.LOW)
def verfar2():
    GPIO.output(36,GPIO.HIGH)
    GPIO.output(38,GPIO.LOW)
    sleep(0.25)
    GPIO.output(36,GPIO.LOW)
def horback1():
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(18,GPIO.LOW)
def horback2():
    GPIO.output(16,GPIO.LOW)
    GPIO.output(18,GPIO.HIGH)
    sleep(0.25)
    GPIO.output(18,GPIO.LOW)
def verback1():
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(38,GPIO.LOW)
def verback2():
    GPIO.output(36,GPIO.LOW)
    GPIO.output(38,GPIO.HIGH)
    sleep(0.25)
    GPIO.output(38,GPIO.LOW)
