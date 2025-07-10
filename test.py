import RPi.GPIO as GPIO
import time

# TB6612 GPIO 引脚定义
AIN1 = 17       # 电机方向 1
AIN2 = 27       # 电机方向 2
PWMA = 22       # PWM 控制速度
STBY = 5        # 使能引脚

# 初始化 GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

pwm = GPIO.PWM(PWMA, 1000)  # 1kHz PWM 频率
pwm.start(0)

# 启用驱动板
GPIO.output(STBY, GPIO.HIGH)

def motor_forward(speed=80):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

try:
    print("开始正转 50 秒")
    motor_forward(speed=80)
    time.sleep(50)

    print("停止电机")
    motor_stop()

except KeyboardInterrupt:
    print("中断程序")

finally:
    motor_stop()
    pwm.stop()
    GPIO.cleanup()
