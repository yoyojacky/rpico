from machine import Pin, I2C
import time


led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)   
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)   
interval = 0.1

while True:
    led0.value(1)
    time.sleep(interval)
    led1.value(1)
    time.sleep(interval)
    led2.value(1)
    time.sleep(interval)
    led3.value(1)
    time.sleep(interval)
    led4.value(1)
    time.sleep(interval)
    led5.value(1)
    time.sleep(interval)
    
    led0.value(0)
    time.sleep(interval)
    led1.value(0)
    time.sleep(interval)
    led2.value(0)
    time.sleep(interval)
    led3.value(0)
    time.sleep(interval)
    led4.value(0)
    time.sleep(interval)
    led5.value(0)
    time.sleep(interval)
