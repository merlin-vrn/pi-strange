#!/usr/bin/python3
# coding: utf-8

from RPi import GPIO
import time
import math
from random import uniform

# Pin9  = GND
# Pin11 = GPIO17
# Pin13 = GPIO27
LAMPs = [17, 27]

PWMFREQ = 50
FREQ = 50

DT = 0.0001
S = 5
R = 15
B = 1

X_RANGE = (-9.7138, 9.2645)
Y_RANGE = (-13.4565, 12.6104)
Z_RANGE = (0.43836, 24.9227)

def lorenz_attractor(x0, y0, z0):
    x = x0
    y = y0
    z = z0

    while True:
        x1 = x +   S*(y-x)     * DT
        y1 = y + ( x*(R-z)-y ) * DT
        z1 = z + ( x*y-B*z   ) * DT
        yield (x,y,z)
        x = x1
        y = y1
        z = z1
        
def sane_scale(x, xmin, xmax):
    if x > xmax:
        return 1
    elif x < xmin:
        return 0
    return (x - xmin)/(xmax - xmin)

def main():
    GPIO.setmode(GPIO.BCM)

    pwm = {}
    dcg = {}
    for LAMP in LAMPs:
        GPIO.setup(LAMP, GPIO.OUT)

        pwm[LAMP] = GPIO.PWM(LAMP, PWMFREQ)
        pwm[LAMP].start(0)

        dcg[LAMP] = lorenz_attractor(uniform(*X_RANGE), uniform(*Y_RANGE), uniform(*Z_RANGE))

    try:
        while True:
            for LAMP in LAMPs:
                val = dcg[LAMP].__next()
                pwm[LAMP].ChangeDutyCycle(sane_scale(val[0], *X_RANGE) * 100)
            time.sleep(1/FREQ)

    except KeyboardInterrupt:
        pass

    for LAMP in LAMPs:
        pwm[LAMP].stop()
        GPIO.output(LAMP, False)

    GPIO.cleanup()

if __name__ == '__main__':
    main()
