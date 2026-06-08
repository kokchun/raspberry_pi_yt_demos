import time 
from machine import Pin

time.sleep(.1)

led = Pin(15, Pin.OUT)

print(led)
print(Pin.OUT)

while True:
    led.toggle()
    time.sleep(3)