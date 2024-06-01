#!/usr/bin/env python
from smbus import SMBus

sla = 0x08
bus = SMBus(1)

print("read_byte_data")
rtn = bus.read_byte_data(sla, 0x12)
print(rtn)

print("read_i2c_block_data")
rtn = bus.read_i2c_block_data(sla, 0x12, 16)
print(rtn)
