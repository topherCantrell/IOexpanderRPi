import time
import smbus

CHIP_A = 0x3E # I2C address for chip A
CHIP_B = 0x3B # I2C address for chip B

SX_RegPullDownA = 0x09 # Registers to enable ...
SX_RegPullDownB = 0x08 # ... pulldown resistors

SX_RegDirA = 0x0F # Data direction ...
SX_RegDirB = 0x0E # ... registers

SX_RegDataA = 0x11 # Data value ...
SX_RegDataB = 0x10 # ... registers

bus = smbus.SMBus(1)

# Pull-down resistors on all inputs
bus.write_byte_data(CHIP_A,SX_RegPullDownA,0xFF)
bus.write_byte_data(CHIP_A,SX_RegPullDownB,0xFF)
bus.write_byte_data(CHIP_B,SX_RegPullDownA,0xFF)
bus.write_byte_data(CHIP_B,SX_RegPullDownB,0xFF)

# When a pin becomes an output, make it high
bus.write_byte_data(CHIP_A,SX_RegDataA,0xFF)
bus.write_byte_data(CHIP_A,SX_RegDataB,0xFF)
bus.write_byte_data(CHIP_B,SX_RegDataA,0xFF)
bus.write_byte_data(CHIP_B,SX_RegDataB,0xFF)

def _decode_line(x):
    # Is this pin on chip A or chip B?
    # Is it register A or register B on that chip?
    # What is the bit-mask for the pin in that register?
    # Answer all these questions and return the results.
    if x<16:
        addr = CHIP_A # 0..15    : Chip A
    else:
        addr = CHIP_B # 16 .. 31 : Chip B
        x = x & 0x0F
    if x<8:
        reg_ofs = 0 # 0..7   : Register A
    else:
        reg_ofs = -1 # 8..15 : All of the B regs are one less than the A regs
        x = x & 0x07
    mask = 1 << x # Convert bit number to bit mask
    return (addr,reg_ofs,mask)

def set_line_input(x):
    # Make pin X an input (with pulldown resistor)
    addr,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(addr,SX_RegDirA+reg_ofs)
    v = v | mask # Change bit to a 1 (input)
    bus.write_byte_data(addr,SX_RegDirA+reg_ofs,v)   
    
def set_line_output(x):
    # Make pin X an output (with output value 1)
    addr,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(addr,SX_RegDirA+reg_ofs)
    v = v & (!mask) # Change bit to a 0 (output)
    bus.write_byte_data(addr,SX_RegDirA+reg_ofs,v)   

def is_line_high(x):
    # Return True if pin X is input 1
    addr,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(addr,SX_RegDirA+reg_ofs)
    return (v & mask)!=0

def sweep():
    # Run the grid and see what lines are shorted together
    for x in range(32):
        set_line_output(x)
        time.sleep(0.01)
        for y in range(32):
            if y!=x:
                if is_line_high(y):
                    print('(%d,%d)' % (x,y),end='')
        set_line_input(x)
        time.sleep(0.01)    

if __name__ == "__main__":
    
    # Initialize all pins to inputs with pulldowns
    for x in range(32):
        set_line_input(x)

    # Continually sweep the matrix looking for hits
    while True:
        sweep()
