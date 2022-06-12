import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 18
ECHO = 23
buzzer = 24

print(" Now beggingin the Distance Measurements")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
Buzzerlow = GPIO.PWM(buzzer, 1)
i = 0


while True:
    GPIO.output(TRIG, False)
    time.sleep(1)
    GPIO.output(TRIG, True)
    time.sleep(0.01)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*1150
    distance = round(distance,2)
    safetyDistance = distance


    if 2<= safetyDistance <= 7:
        print(safetyDistance)
        print("Buzzer is now On")
        Buzzerlow.ChangeFrequency(50)
        Buzzerlow.start(50)
        

        
    elif safetyDistance < 2:
        print("OBJECT IS REALLY CLOSE")
        print(safetyDistance)
        Buzzerlow.ChangeFrequency(100)
        Buzzerlow.start(50)
        
    else:
        print("Distance in cm: ")
        print(safetyDistance)
        
        print("Buzzer is now Off")
        Buzzerlow.stop()
