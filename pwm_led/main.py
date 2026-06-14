from machine import Pin, PWM
import time 
from constants import MAX_U16


time.sleep(.5)

led_ref = Pin(14, Pin.OUT)
led_ref.value(1)

led_pwm = PWM(Pin(15))
led_pwm.freq(1000)

i = 1 

while True:
    i *= 2
    led_pwm.duty_u16(int(MAX_U16/i))

    print(f"duty cycle {100/i}%")
    if i > 16: 
        i = 1

    time.sleep(2)
