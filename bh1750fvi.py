import time

OP_SINGLE_HRES1 = 0x20
OP_SINGLE_HRES2 = 0x21
OP_SINGLE_LRES = 0x23

DELAY_HMODE = 120000  # 120ms in H-mode
DELAY_LMODE = 16000  # 16ms in L-mode


def sample(i2c, mode=OP_SINGLE_HRES1, i2c_addr=0x23):
    """
        Performs a single sampling. returns the result in lux
    """

    i2c.writeto(i2c_addr, b"\x00")  # make sure device is in a clean state
    i2c.writeto(i2c_addr, b"\x01")  # power up
    i2c.writeto(i2c_addr, bytes([mode]))  # set measurement mode

    time.sleep_us(DELAY_LMODE if mode == OP_SINGLE_LRES else DELAY_HMODE)

    raw = i2c.readfrom(i2c_addr, 2)
    i2c.writeto(i2c_addr, b"\x00")  # power down again

    # we must divide the end result by 1.2 to get the lux
    return ((raw[0] << 24) | (raw[1] << 16)) // 78642
