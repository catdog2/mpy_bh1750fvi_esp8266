bh1750fvi driver for micropython on esp8266
###########################################

Example::

    import bh1750fvi
    from machine import I2C,Pin
    i2c = I2C(Pin(5),Pin(4))
    result = bh1750fvi.sample(i2c) # in lux

