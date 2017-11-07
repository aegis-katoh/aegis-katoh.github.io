import smbus
import time
i2c = smbus.SMBus(1)
addr = 0x68
Vref = 2.048
config = 0b10011000

i2c.write_byte(addr, config)
time.sleep(0.2)

def swap16(x):
	return (((x << 8) & 0xFF00) | ((x >> 8) & 0x00FF))

def sign16(x):
	return ( -(x & 0b1000000000000000) | (x & 0b0111111111111111))

# main
while 1:
	data = i2c.read_word_data(addr, config)
	raw = swap16(int(hex(data),16))
	raw_s = sign16(int(hex(raw),16))
	volts = round((Vref * raw_s / 32767), 4)
	print (volts)
	time.sleep(1)

