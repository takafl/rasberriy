from gpiozero import Servo,LED
from time import sleep

# إعداد محرك السيرفو على البن رقم 17 (يمكنك تغيير رقم البن حسب الحاجة)
servo = Servo(27)
p16=LED()
p16.on()

try:
    while True:
        # تحريك السيرفو إلى أقصى اليسار
        servo.min()
        print("Servo is at min position.")
        
        

except KeyboardInterrupt:
    # تحرير الموارد عند انتهاء البرنامج أو عند مقاطعة المستخدم
    print("Exiting program.")
finally:
    # التأكد من تحرير الموارد عند النهاية
    servo.close()
    p16.close()
