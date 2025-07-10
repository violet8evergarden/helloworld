import RPi.GPIO as GPIO
import time
from motor import Motor
from ultrasonic import Ultrasonic

# 设置 GPIO 模式
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 引脚定义（如需调整请根据实际连线）
AIN1 = 17
AIN2 = 27
PWMA = 22
STBY = 5

TRIG = 23
ECHO = 24

# 创建对象
motor = Motor(AIN1, AIN2, PWMA, STBY)
ultra = Ultrasonic(TRIG, ECHO)

TARGET_HEIGHT_CM = 100

try:
    while True:
        dist = ultra.get_distance()
        print(f"当前高度: {dist} cm")

        if dist > TARGET_HEIGHT_CM:
            motor.move_up(80)
        else:
            print("到达 2 米，停止电机")
            motor.stop()
            break

        time.sleep(0.1)

except KeyboardInterrupt:
    print("用户中断程序")

finally:
    motor.stop()
    GPIO.cleanup()
