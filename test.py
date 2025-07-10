import RPi.GPIO as GPIO
import time

# TB6612 GPIO 引脚定义（你可以根据需要调整）
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

pwm = GPIO.PWM(PWMA, 1000)  # 频率 1kHz
pwm.start(0)

# 启用电机驱动
GPIO.output(STBY, GPIO.HIGH)

def motor_forward(speed=80):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def motor_backward(speed=80):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)

def motor_stop():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

try:
    print("电机正转")
    motor_forward(80)
    time.sleep(2)

    print("电机反转")
    motor_backward(80)
    time.sleep(2)

    print("停止电机")
    motor_stop()

except KeyboardInterrupt:
    print("中断程序")

finally:
    motor_stop()
    pwm.stop()
    GPIO.cleanup()