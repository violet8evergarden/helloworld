import RPi.GPIO as GPIO
import time

# 设置引脚映射（BCM 模式）
MotorA = {"IN1": 17, "IN2": 27, "PWM": 22}
MotorB = {"IN1": 6,  "IN2": 13, "PWM": 19}
STBY = 5

def setup():
    GPIO.setmode(GPIO.BCM)
    pins = list(MotorA.values()) + list(MotorB.values()) + [STBY]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    # 启动 PWM
    global pwmA, pwmB
    pwmA = GPIO.PWM(MotorA["PWM"], 1000)  # 1kHz
    pwmB = GPIO.PWM(MotorB["PWM"], 1000)
    pwmA.start(0)
    pwmB.start(0)

def run_motor(motor, speed=100):
    GPIO.output(motor["IN1"], GPIO.HIGH)
    GPIO.output(motor["IN2"], GPIO.LOW)
    if motor == MotorA:
        pwmA.ChangeDutyCycle(speed)
    else:
        pwmB.ChangeDutyCycle(speed)

def stop_motor(motor):
    GPIO.output(motor["IN1"], GPIO.LOW)
    GPIO.output(motor["IN2"], GPIO.LOW)
    if motor == MotorA:
        pwmA.ChangeDutyCycle(0)
    else:
        pwmB.ChangeDutyCycle(0)

def main():
    setup()
    GPIO.output(STBY, GPIO.HIGH)  # 使能 TB6612

    print("Motor A and B running...")
    run_motor(MotorA, speed=80)
    run_motor(MotorB, speed=80)

    time.sleep(5)

    print("Stopping motors...")
    stop_motor(MotorA)
    stop_motor(MotorB)

    pwmA.stop()
    pwmB.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
