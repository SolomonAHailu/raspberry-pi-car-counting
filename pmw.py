import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor 1 pins
enable_pin1 = 18
input1_pin1 = 23
input2_pin1 = 24

# Motor 2 pins
enable_pin2 = 12
input1_pin2 = 27
input2_pin2 = 22

# Setup pins
GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(input1_pin1, GPIO.OUT)
GPIO.setup(input2_pin1, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)
GPIO.setup(input1_pin2, GPIO.OUT)
GPIO.setup(input2_pin2, GPIO.OUT)

# Setup PWM
pwm1 = GPIO.PWM(enable_pin1, 100)  # 100 Hz frequency
pwm2 = GPIO.PWM(enable_pin2, 100)
pwm1.start(0)
pwm2.start(0)

def motor_control(motor, speed, direction):
    if motor == 1:
        pwm = pwm1
        input1 = input1_pin1
        input2 = input2_pin1
    else:
        pwm = pwm2
        input1 = input1_pin2
        input2 = input2_pin2
    
    if direction == 'forward':
        GPIO.output(input1, True)
        GPIO.output(input2, False)
    elif direction == 'reverse':
        GPIO.output(input1, False)
        GPIO.output(input2, True)
    else:
        pwm.ChangeDutyCycle(0)
        return
    
    pwm.ChangeDutyCycle(speed)

try:
    while True:
        motor_control(1, 70, 'forward')
        motor_control(2, 70, 'forward')
        time.sleep(2)
        motor_control(1, 50, 'reverse')
        motor_control(2, 50, 'reverse')
        time.sleep(2)
        motor_control(1, 0, 'stop')
        motor_control(2, 0, 'stop')
        time.sleep(1)
except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
