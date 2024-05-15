from gpiozero import PWMOutputDevice
import time

# إنشاء كائن PWM مرتبط بالبن رقم 27
pwm = PWMOutputDevice(27)

# تعريف دالة لتعيين قيمة PWM
def set_pwm_value(value):
    if value in [50, 25, 75, 100]:
        pwm.value = value / 100
    else:
        print("Invalid PWM value. Please use 25, 50, 75, or 100.")

try:
    while True:
        # تعيين القيم المحددة بشكل متتابع
        for value in [50, 25, 75, 100]:
            set_pwm_value(value)
            time.sleep(1)
except Exception as e:
    print(e)
