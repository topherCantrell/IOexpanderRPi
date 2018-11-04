import smbus
import time

CHIP_A = 0x3E # I2C address for chip A
CHIP_B = 0x3F # I2C address for chip B

SX_RegDirA = 0x0F # Data direction ...
SX_RegDirB = 0x0E # ... registers

SX_RegDataA = 0x11 # Data value ...
SX_RegDataB = 0x10 # ... registers

SX_RegPullDownA = 0x09 # Registers to enable ...
SX_RegPullDownB = 0x08 # ... pulldown resistors

# Green circuit board below keypad: * 1 2 3 4 5 6 7 *
#
KEY_ROW_1 = 4 #  --1 2 3    Board pin 2
KEY_ROW_2 = 7 #  --4 5 6    Board pin 7 (far right)         
KEY_ROW_3 = 6 #  --7 8 9    Board pin 6              
KEY_ROW_4 = 5 #  --# 0 *    Board pin 4
#                  | | |
KEY_COL_1 = 9  # --+ | |    Board pin 3
KEY_COL_2 = 8  # ----+ |    Board pin 1 (far left)
KEY_COL_3 = 10 # ------+    Board pin 5

bus = smbus.SMBus(1)

# RED LED on Pin 11 of Chip A
#
# All ones (inputs) except pin 11 (output)
bus.write_byte_data(CHIP_A,SX_RegDirB,0xFF-8)
# Turn on pin 11
bus.write_byte_data(CHIP_A,SX_RegDataB,8)
time.sleep(1)
bus.write_byte_data(CHIP_A,SX_RegDataB,0)


# GREEN LED on Pin 11 of Chip B
#
# All ones (inputs) except pin 11 (output)
bus.write_byte_data(CHIP_B,SX_RegDirB,0xFF-8)
# Turn on pin 11
bus.write_byte_data(CHIP_B,SX_RegDataB,8)
time.sleep(1)
bus.write_byte_data(CHIP_B,SX_RegDataB,0)


# Write a HIGH to a single column
bus.write_byte_data(CHIP_B,SX_RegDirA,0xFF-64)
bus.write_byte_data(CHIP_B,SX_RegDataA,64)

# Read all the states from the row
bus.write_byte_data(CHIP_B,SX_RegDirB,0xFF)
bus.write_byte_data(CHIP_B,SX_RegPullDownB,0xFF)

while True:
    a = bus.read_byte_data(CHIP_B,SX_RegDataB)
    print(a)
    time.sleep(1)

