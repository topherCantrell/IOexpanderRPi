import time
import smbus

SX_RegPullDownA = 0x09 # Registers to enable ...
SX_RegPullDownB = 0x08 # ... pulldown resistors

SX_RegDirA = 0x0F # Data direction ...
SX_RegDirB = 0x0E # ... registers

SX_RegDataA = 0x11 # Data value ...
SX_RegDataB = 0x10 # ... registers

bus = smbus.SMBus(1)

CHIP_I2C_ADDR = [0x3E,0x3F]

PINS = [16+4, 16+5, 16+6, 16+7, 16+8, 16+9, 16+10] 

def _decode_line(x):
    # Is this pin on chip A or chip B?
    # Is it register A or register B on that chip?
    # What is the bit-mask for the pin in that register?
    # Answer all these questions and return the results.
    if x<16:
        chip = 0 # 0..15    : Chip A
    else:
        chip = 1 # 16 .. 31 : Chip B
        x = x & 0x0F
    if x<8:
        reg_ofs = 0 # 0..7   : Register A
    else:
        reg_ofs = -1 # 8..15 : All of the B regs are one less than the A regsset
        x = x & 0x07
    mask = 1 << x # Convert bit number to bit mask
    return (chip,reg_ofs,mask)

def set_line_input_pulldown(x):
    # Make pin X an input (with pulldown resistor)
    chip,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(CHIP_I2C_ADDR[chip],SX_RegDirA+reg_ofs)
    v = v | mask # Change bit to a 1 (input)
    bus.write_byte_data(CHIP_I2C_ADDR[chip],SX_RegDirA+reg_ofs,v)
    #
    v = bus.read_byte_data(CHIP_I2C_ADDR[chip],SX_RegPullDownA+reg_ofs)
    v = v | mask # Change bit to a 1 (pulldown)
    bus.write_byte_data(CHIP_I2C_ADDR[chip],SX_RegPullDownA+reg_ofs,v)   
    
def set_line_output_high(x):
    # Make pin X an output (with output value 1)
    chip,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(CHIP_I2C_ADDR[chip],SX_RegDirA+reg_ofs)
    v = v & ((~mask)&0xFF) # Change bit to a 0 (output)
    bus.write_byte_data(CHIP_I2C_ADDR[chip],SX_RegDirA+reg_ofs,v)    
    #
    v = bus.read_byte_data(CHIP_I2C_ADDR[chip],SX_RegDataA+reg_ofs)
    v = v | mask # Change bit to a 1 (output high)
    bus.write_byte_data(CHIP_I2C_ADDR[chip],SX_RegDataA+reg_ofs,v)   

def is_line_high(x):
    # Return True if pin X is input 1
    chip,reg_ofs,mask = _decode_line(x)
    v = bus.read_byte_data(CHIP_I2C_ADDR[chip],SX_RegDataA+reg_ofs)
    return (v & mask)!=0

def sweep():
    # Run the grid and see what lines are shorted together
    for x in PINS:
        set_line_output_high(x)
        time.sleep(0.01)
        for y in PINS:
            if y!=x:
                if is_line_high(y):
                    print('(%d,%d)' % (x,y),end='')
        set_line_input_pulldown(x)
        time.sleep(0.01)   
    print('') 

if __name__ == "__main__":    
    
    # Initialize all pins to inputs with pulldowns
    for x in PINS:
        set_line_input_pulldown(x)

    # Continually sweep the matrix looking for hits
    while True:
        sweep()
