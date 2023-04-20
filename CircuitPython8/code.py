# SPDX-FileCopyrightText: 2021 Ruiz Bros for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example displays soolid white and rainbox.
"""
import time
import board
import neopixel
from adafruit_led_animation.color import WHITE
from rainbowio import colorwheel

pixel_pin = board.D0  # Pin connected to your NeoPixels
pixel_num = 8  # Number of NeoPixels you have connected
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.8, auto_write=False)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(pixel_num):
            rc_index = (i * 256 // pixel_num) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    pixels.fill(WHITE)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(5)
    '''
    '''
    for i in range(5):
        rainbow_cycle(0.01)  # Increase the number to slow down the rainbow
