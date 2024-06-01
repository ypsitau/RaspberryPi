#!/usr/bin/env python
import smbus

sla = 0x08
bus = smbus.SMBus(1)

print("write_byte_data")
bus.write_byte_data(sla, 0x12, 0x34)

print("write_i2c_block_data")
bus.write_i2c_block_data(sla, 0x12, [1, 2, 3, 4, 5, 6])
