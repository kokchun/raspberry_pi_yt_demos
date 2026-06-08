from machine import Pin
import time

time.sleep(0.1)

led = dict(
    red=Pin(15, Pin.OUT),
    yellow=Pin(13, Pin.OUT),
    green=Pin(10, Pin.OUT),
)


colors = ("red", "yellow", "green")
durations = (2,1,3)

while True:
    for color, duration in zip(colors, durations):

        led[color].value(1)
        remaining_colors = tuple(c for c in colors if c != color)

        # turn off the other LEDs
        led[remaining_colors[0]].value(0)
        led[remaining_colors[1]].value(0)

        time.sleep(duration)