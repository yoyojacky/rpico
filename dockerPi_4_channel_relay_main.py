from machine import Pin, I2C
import time



i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)

print(i2c.scan())

while True:
    for i in range(1,5):
        i2c.writeto_mem(16,i,bytes([0xff]))
        time.sleep(1)
        i2c.writeto_mem(16,i,bytes([0x00]))
        time.sleep(1)
    
        

