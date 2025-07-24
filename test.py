import RPi.GPIO as GPIO
import time

# 电机控制引脚
MOTORS = {
    "A": {"IN1": 17, "IN2": 27, "PWM": 22},
    "B": {"IN1": 5,  "IN2": 6,  "PWM": 13},
}

def setup():
    GPIO.setmode(GPIO.BCM)
    for m in MOTORS.values():
        GPIO.setup(m["IN1"], GPIO.OUT)
        GPIO.setup(m["IN2"], GPIO.OUT)
        GPIO.setup(m["PWM"], GPIO.OUT)
        m["pwm"] = GPIO.PWM(m["PWM"], 1000)  # 1kHz PWM
        m["pwm"].start(0)

def move_motor(name, speed, direction):
    m = MOTORS[name]
    GPIO.output(m["IN1"], GPIO.HIGH if direction == "forward" else GPIO.LOW)
    GPIO.output(m["IN2"], GPIO.LOW if direction == "forward" else GPIO.HIGH)
    m["pwm"].ChangeDutyCycle(speed)

def stop_motor(name):
    m = MOTORS[name]
    m["pwm"].ChangeDutyCycle(0)
    GPIO.output(m["IN1"], GPIO.LOW)
    GPIO.output(m["IN2"], GPIO.LOW)

def cleanup():
    for m in MOTORS.values():
        m["pwm"].stop()
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()
        print("Motor A forward 70%")
        move_motor("A", 70, "forward")
        print("Motor B backward 50%")
        move_motor("B", 50, "backward")
        time.sleep(5)

        print("Stopping motors")
        stop_motor("A")
        stop_motor("B")
    finally:
        cleanup()
