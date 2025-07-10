import RPi.GPIO as GPIO
import time

# ---------------------------
# GPIO 引脚定义
# ---------------------------
AIN1 = 17    # 电机A方向
AIN2 = 27
PWMA = 22

BIN1 = 6     # 电机B方向
BIN2 = 13
PWMB = 19

STBY = 5     # 使能引脚

# ---------------------------
# GPIO 初始化
# ---------------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_pins = [AIN1, AIN2, PWMA, BIN1, BIN2, PWMB, STBY]
for pin in motor_pins:
    GPIO.setup(pin, GPIO.OUT)

pwm_a = GPIO.PWM(PWMA, 1000)
pwm_b = GPIO.PWM(PWMB, 1000)

pwm_a.start(0)
pwm_b.start(0)

# ---------------------------
# 电机控制函数
# ---------------------------
def enable_motor():
    GPIO.output(STBY, GPIO.HIGH)

def disable_motor():
    GPIO.output(STBY, GPIO.LOW)

def motor_a_forward(speed=80):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(speed)

def motor_b_forward(speed=80):
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_b.ChangeDutyCycle(speed)

def stop_all():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.LOW)
    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)
    disable_motor()

# ---------------------------
# 主程序：两个电机正转 5 秒
# ---------------------------
try:
    print("启动两个电机正转 5 秒")
    enable_motor()
    motor_a_forward(80)
    motor_b_forward(80)

    time.sleep(5)

    print("停止两个电机")
    stop_all()

except KeyboardInterrupt:
    print("用户中断")

finally:
    stop_all()
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
