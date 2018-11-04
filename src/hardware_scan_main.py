import smbus
import time

SX_RegPullUpB = 0x06
SX_RegPullUpA = 0x07

SX_RegPullDownA = 0x09 # Registers to enable ...
SX_RegPullDownB = 0x08 # ... pulldown resistors

SX_RegDirA = 0x0F # Data direction ...
SX_RegDirB = 0x0E # ... registers

SX_RegDataA = 0x11 # Data value ...
SX_RegDataB = 0x10 # ... registers

SX_RegOpenDrainA = 0x0B
SX_RegOpenDrainB = 0x0A

SX_RegDebounceConfig = 0x22
SX_RegDebounceEnableB = 0x23
SX_RegDebounceEnableA = 0x24
SX_RegKeyConfig1 = 0x25
SX_RegKeyConfig2 = 0x26
SX_RegKeyData1 = 0x27
SX_RegKeyData2 = 0x28

bus = smbus.SMBus(1)

CHIP_I2C_ADDR = [0x3E,0x3F]

KEY_ROW_1 = 0 #  --1 2 3    Board pin 2
KEY_ROW_2 = 3 #  --4 5 6    Board pin 7 (far right)         
KEY_ROW_3 = 2 #  --7 8 9    Board pin 6              
KEY_ROW_4 = 1 #  --# 0 *    Board pin 4
#                  | | |
KEY_COL_1 = 9  # --+ | |    Board pin 3
KEY_COL_2 = 8  # ----+ |    Board pin 1 (far left)
KEY_COL_3 = 10 # ------+    Board pin 5

# A x  x  x  x  x  x  x  x
#   *  *  *  *  R2 R3 R4 R1

# B x  x  x  x  x  x  x  x
#   *  *  *  *  *  C3 C1 C2

# Rows are outputs with open-drain
bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegDirA,       0b11110000) # 00001111 0's are outputs
#bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegOpenDrainA, 0b00001111) # 11110000 1's are on

# Columns are inputs with pullups
bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegDirB,       0b11111111) # 11110111 0's are outputs
bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegPullUpB,    0b11111111) # 0000111 1's are pulled up 

#bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegKeyConfig2, 0b00011010) # 00_011_010 4 rows and 3 columns

# You could watch the NINT interrupt line, or you could poll like this:

bus.write_byte_data(CHIP_I2C_ADDR[1],SX_RegDataA, 0x00)

while True:
    rows = bus.read_byte_data(CHIP_I2C_ADDR[1],SX_RegDataB)
    print('>>'+str(rows)+"<<")
    time.sleep(1)

"""
while True:
    cols = bus.read_byte_data(CHIP_I2C_ADDR[1],SX_RegKeyData1)
    print('>'+str(cols))
    if cols!=0xFF:
        rows = bus.read_byte_data(CHIP_I2C_ADDR[1],SX_RegKeyData2)
        print('::'+str(cols)+':'+str(rows)+'::')
    time.sleep(0.5)
"""    