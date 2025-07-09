import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def get_distance(self):
        GPIO.output(self.trig, False)
        time.sleep(0.05)

        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()

        duration = pulse_end - pulse_start
        distance_cm = duration * 17150
        return round(distance_cm, 2)
