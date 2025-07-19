import RPi.GPIO as GPIO
import time

# 电机控制引脚映射表
MOTORS = {
    "A": {"IN1": 17, "IN2": 27, "PWM": 22},
    "B": {"IN1": 6,  "IN2": 13, "PWM": 19},
    "C": {"IN1": 16, "IN2": 20, "PWM": 21},
    "D": {"IN1": 23, "IN2": 24, "PWM": 25},
}

STBY_A = 5
STBY_B = 12

def setup():
    GPIO.setmode(GPIO.BCM)
    for m in MOTORS.values():
        GPIO.setup(m["IN1"], GPIO.OUT)
        GPIO.setup(m["IN2"], GPIO.OUT)
        GPIO.setup(m["PWM"], GPIO.OUT)
    GPIO.setup(STBY_A, GPIO.OUT)
    GPIO.setup(STBY_B, GPIO.OUT)

    global PWMS
    PWMS = {name: GPIO.PWM(cfg["PWM"], 1000) for name, cfg in MOTORS.items()}
    for pwm in PWMS.values():
        pwm.start(0)

def run_motor(name, speed=100):
    cfg = MOTORS[name]
    GPIO.output(cfg["IN1"], GPIO.HIGH)
    GPIO.output(cfg["IN2"], GPIO.LOW)
    PWMS[name].ChangeDutyCycle(speed)

def stop_motor(name):
    cfg = MOTORS[name]
    GPIO.output(cfg["IN1"], GPIO.LOW)
    GPIO.output(cfg["IN2"], GPIO.LOW)
    PWMS[name].ChangeDutyCycle(0)

def main():
    setup()
    GPIO.output(STBY_A, GPIO.HIGH)
    GPIO.output(STBY_B, GPIO.HIGH)

    print("All motors running forward...")
    for name in MOTORS:
        run_motor(name)

    time.sleep(5)

    print("All motors stopping...")
    for name in MOTORS:
        stop_motor(name)

    for pwm in PWMS.values():
        pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
