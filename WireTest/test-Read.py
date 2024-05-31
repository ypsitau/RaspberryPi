#!/usr/bin/env python
import smbus

sla = 0x70
bus = smbus.SMBus(1)
#bus.write_byte_data(sla, 0x12, 0x13)
value = bus.read_byte_data(sla, 0x45)
print("%x" % value)
