








import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor 1 pins
enable_pin1 = 24 #19
input1_pin1 = 16 #2
input2_pin1 = 12 #3

# Motor 2 pins
enable_pin2 = 25 #13
input1_pin2 = 21 #4
input2_pin2 = 20 #17

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

def set_motor_speed1(speed1):
    """ Adjust the motor speed between 0% and 100% """
    pwm1.ChangeDutyCycle(speed1)
   
def set_motor_speed2(speed2):
    """ Adjust the motor speed between 0% and 100% """
    pwm2.ChangeDutyCycle(speed2)
      
def forward(tf):
    GPIO.output(input1_pin1, True)
    GPIO.output(input2_pin1, False)
    GPIO.output(input1_pin2, True)
    GPIO.output(input2_pin2, False)  
    time.sleep(tf)

def reverse(tf):
    GPIO.output(input1_pin1, False)
    GPIO.output(input2_pin1, True)
    GPIO.output(input1_pin2, False)
    GPIO.output(input2_pin2, True)  
    time.sleep(tf)

def left(tf):
    GPIO.output(input1_pin1, True)
    GPIO.output(input2_pin1, False)
    GPIO.output(input1_pin2, False)
    GPIO.output(input2_pin2, False)  
    time.sleep(tf)

def right(tf):
    GPIO.output(input1_pin1, False)
    GPIO.output(input2_pin1, False)
    GPIO.output(input1_pin2, True)
    GPIO.output(input2_pin2, False)  
    time.sleep(tf)

# Example usage
#set_motor_speed1(40)
#set_motor_speed2(80)
#forward(2)
#reverse(2)
#left(2)
#right(2)
#GPIO.cleanup()
