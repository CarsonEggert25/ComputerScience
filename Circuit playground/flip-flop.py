from adafruit_circuitplayground import cp
import time
cp.pixels.brightness = 0.05
while True:
    if cp.switch:

        cp.pixels[0] =(0,255,0)
        cp.pixels[1] =(0,255,0)
        cp.pixels[2] =(0,255,0)
        cp.pixels[3] =(0,255,0)
        cp.pixels[4] =(0,255,0)
        cp.pixels[5] =(0,0,0)
        cp.pixels[6] =(0,0,0)
        cp.pixels[7] =(0,0,0)
        cp.pixels[8] =(0,0,0)
        cp.pixels[9] =(0,0,0)
    else:
        cp.pixels[0] =(0,0,0)
        cp.pixels[1] =(0,0,0)
        cp.pixels[2] =(0,0,0)
        cp.pixels[3] =(0,0,0)
        cp.pixels[4] =(0,0,0)
        cp.pixels[5] =(0,255,0)
        cp.pixels[6] =(0,255,0)
        cp.pixels[7] =(0,255,0)
        cp.pixels[8] =(0,255,0)
        cp.pixels[9] =(0,255,0)