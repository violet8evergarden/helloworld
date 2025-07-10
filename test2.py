import RPi.GPIO as GPIO
import time

BIN1 = 6
BIN2 = 13
PWMB = 19
STBY = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)

pwm_b = GPIO.PWM(PWMB, 1000)
pwm_b.start(0)

print("启动 B 电机正转")
GPIO.output(STBY, GPIO.HIGH)
GPIO.output(BIN1, GPIO.HIGH)
GPIO.output(BIN2, GPIO.LOW)
pwm_b.ChangeDutyCycle(80)

time.sleep(3)

print("停止 B 电机")
GPIO.output(BIN1, GPIO.LOW)
GPIO.output(BIN2, GPIO.LOW)
pwm_b.ChangeDutyCycle(0)
GPIO.output(STBY, GPIO.LOW)

pwm_b.stop()
GPIO.cleanup()