#!/usr/bin/env python
import smbus

addr = 0x08
bus = smbus.SMBus(1)
value = bus.read_i2c_block_data(addr, 0x39)
print('%02x %02x %02x %02x %02x %02x' % (value[0], value[1], value[2], value[3], value[4], value[5]))
#bus.write_byte_data(addr, 0x39, 0xe7)
