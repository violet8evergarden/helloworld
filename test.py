import RPi.GPIO as GPIO
import time

# 电机引脚定义
MOTOR_A = {'IN1': 17, 'IN2': 27, 'ENA': 22}
MOTOR_B = {'IN1': 6,  'IN2': 13, 'ENA': 19}

# PWM 频率
PWM_FREQ = 1000

def setup_motor_pins(motor):
    GPIO.setup(motor['IN1'], GPIO.OUT)
    GPIO.setup(motor['IN2'], GPIO.OUT)
    GPIO.setup(motor['ENA'], GPIO.OUT)
    pwm = GPIO.PWM(motor['ENA'], PWM_FREQ)
    pwm.start(0)
    return pwm

def run_motor_forward(motor, pwm, speed=100):
    GPIO.output(motor['IN1'], GPIO.HIGH)
    GPIO.output(motor['IN2'], GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def stop_motor(motor, pwm):
    GPIO.output(motor['IN1'], GPIO.LOW)
    GPIO.output(motor['IN2'], GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # 设置电机引脚
    pwm_a = setup_motor_pins(MOTOR_A)
    pwm_b = setup_motor_pins(MOTOR_B)

    print("Running motors forward for 5 seconds...")
    run_motor_forward(MOTOR_A, pwm_a)
    run_motor_forward(MOTOR_B, pwm_b)

    time.sleep(5)

    print("Stopping motors.")
    stop_motor(MOTOR_A, pwm_a)
    stop_motor(MOTOR_B, pwm_b)

    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
