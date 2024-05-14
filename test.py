from gpiozero import PWMOutputDevice
pwm=PWMOutputDevice(27)
import time
try:
    while True:
        for i in range(0,101,5):
            pwm.value=i/100
            time.sleep(0.5)
        for i in range(100,-1,-5):
            pwm.value=i/100
            time.sleep(0.5)
except Exception as e:
    print(e)

