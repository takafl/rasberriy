from gpiozero import Servo
from time import sleep

# إعداد محرك السيرفو على البن رقم 17 (يمكنك تغيير رقم البن حسب الحاجة)
servo = Servo(17)

def move_servo_to(position):
    """
    تحريك محرك السيرفو إلى موضع محدد.
    
    Args:
    position (float): قيمة الموضع بين -1 (أقصى اليسار) و 1 (أقصى اليمين).
    """
    if -1 <= position <= 1:
        servo.value = position
      


try:
    while True:
        # اختبار الدالة مع قيم محددة
        positions = [-1, -0.5, 0, 0.5, 1]
        for pos in range(-100,100,1):
            move_servo_to(pos/100)
            sleep(0.5)
except KeyboardInterrupt:
    # تحرير الموارد عند انتهاء البرنامج أو عند مقاطعة المستخدم
    print("Exiting program.")
finally:
    # التأكد من تحرير الموارد عند النهاية
    servo.close()
