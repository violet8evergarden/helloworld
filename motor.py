import RPi.GPIO as GPIO

class Motor:
    def __init__(self, in1, in2, pwm_pin, stby):
        self.in1 = in1
        self.in2 = in2
        self.pwm_pin = pwm_pin
        self.stby = stby

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        GPIO.setup(self.stby, GPIO.OUT)

        self.pwm = GPIO.PWM(self.pwm_pin, 1000)
        self.pwm.start(0)
        self.stop()

    def enable(self):
        GPIO.output(self.stby, GPIO.HIGH)

    def disable(self):
        GPIO.output(self.stby, GPIO.LOW)

    def move_up(self, speed=80):
        self.enable()
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
        self.disable()
