#!/usr/bin/env python
import pigpio
import time


pi = pigpio.pi()

while True:
    pi.set_PWM_dutycycle(26, 30)
    time.sleep(1)
    pi.set_PWM_dutycycle(26, 0)
    time.sleep(1)

pi.stop()
