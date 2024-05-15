from gpiozero import Servo
from time import sleep

# إعداد محرك السيرفو على البن رقم 17 (يمكنك تغيير رقم البن حسب الحاجة)
servo = Servo(17)

try:
    while True:
        # تحريك السيرفو إلى أقصى اليسار
        servo.min()
        print("Servo is at min position.")
        sleep(1)
        
        # تحريك السيرفو إلى المنتصف
        servo.mid()
        print("Servo is at mid position.")
        sleep(1)
        
        # تحريك السيرفو إلى أقصى اليمين
        servo.max()
        print("Servo is at max position.")
        sleep(1)
        
        # تحريك السيرفو إلى موقع معين (نسبة مئوية)
        positions = [-1, -0.5, 0, 0.5, 1]
        for position in positions:
            servo.value = position
            print(f"Servo is at position {position}.")
            sleep(1)
            
except KeyboardInterrupt:
    # تحرير الموارد عند انتهاء البرنامج أو عند مقاطعة المستخدم
    print("Exiting program.")
finally:
    # التأكد من تحرير الموارد عند النهاية
    servo.close()
