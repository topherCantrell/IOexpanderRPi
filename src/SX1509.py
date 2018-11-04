  
# Device and IO Banks
SX_RegInputDisableB    = 0x00 # Input buffer disable register - I/O[15-8] (Bank B) 0000 0000
SX_RegInputDisableA    = 0x01 # Input buffer disable register - I/O[7-0] (Bank A) 0000 0000
SX_RegLongSlewB        = 0x02 # Output buffer long slew register - I/O[15-8] (Bank B) 0000 0000
SX_RegLongSlewA        = 0x03 # Output buffer long slew register - I/O[7-0] (Bank A) 0000 0000
SX_RegLowDriveB        = 0x04 # Output buffer low drive register - I/O[15-8] (Bank B) 0000 0000
SX_RegLowDriveA        = 0x05 # Output buffer low drive register - I/O[7-0] (Bank A) 0000 0000
SX_RegPullUpB          = 0x06 # Pull-up register - I/O[15-8] (Bank B) 0000 0000
SX_RegPullUpA          = 0x07 # Pull-up register - I/O[7-0] (Bank A) 0000 0000
SX_RegPullDownB        = 0x08 # Pull-down register - I/O[15-8] (Bank B) 0000 0000
SX_RegPullDownA        = 0x09 # Pull-down register - I/O[7-0] (Bank A) 0000 0000
SX_RegOpenDrainB       = 0x0A # Open drain register - I/O[15-8] (Bank B) 0000 0000
SX_RegOpenDrainA       = 0x0B # Open drain register - I/O[7-0] (Bank A) 0000 0000
SX_RegPolarityB        = 0x0C # Polarity register - I/O[15-8] (Bank B) 0000 0000
SX_RegPolarityA        = 0x0D # Polarity register - I/O[7-0] (Bank A) 0000 0000
SX_RegDirB             = 0x0E # Direction register - I/O[15-8] (Bank B) 1111 1111
SX_RegDirA             = 0x0F # Direction register - I/O[7-0] (Bank A) 1111 1111
SX_RegDataB            = 0x10 # Data register - I/O[15-8] (Bank B) 1111 1111*
SX_RegDataA            = 0x11 # Data register - I/O[7-0] (Bank A) 1111 1111*
SX_RegInterruptMaskB   = 0x12 # Interrupt mask register - I/O[15-8] (Bank B) 1111 1111
SX_RegInterruptMaskA   = 0x13 # Interrupt mask register - I/O[7-0] (Bank A) 1111 1111
SX_RegSenseHighB       = 0x14 # Sense register for I/O[15:12] 0000 0000
SX_RegSenseLowB        = 0x15 # Sense register for I/O[11:8] 0000 0000
SX_RegSenseHighA       = 0x16 # Sense register for I/O[7:4] 0000 0000
SX_RegSenseLowA        = 0x17 # Sense register for I/O[3:0] 0000 0000
SX_RegInterruptSourceB = 0x18 # Interrupt source register - I/O[15-8] (Bank B) 0000 0000
SX_RegInterruptSourceA = 0x19 # Interrupt source register - I/O[7-0] (Bank A) 0000 0000
SX_RegEventStatusB     = 0x1A # Event status register - I/O[15-8] (Bank B) 0000 0000
SX_RegEventStatusA     = 0x1B # Event status register - I/O[7-0] (Bank A) 0000 0000
SX_RegLevelShifter1    = 0x1C # Level shifter register 0000 0000
SX_RegLevelShifter2    = 0x1D # Level shifter register 0000 0000
SX_RegClock            = 0x1E # Clock management register 0000 0000
SX_RegMisc             = 0x1F # Miscellaneous device settings register 0000 0000
SX_RegLEDDriverEnableB = 0x20 # LED driver enable register - I/O[15-8] (Bank B) 0000 0000
SX_RegLEDDriverEnableA = 0x21 # LED driver enable register - I/O[7-0] (Bank A) 0000 0000
# 
# Debounce and Keypad Engine
SX_RegDebounceConfig   = 0x22 # Debounce configuration register 0000 0000
SX_RegDebounceEnableB  = 0x23 # Debounce enable register - I/O[15-8] (Bank B) 0000 0000
SX_RegDebounceEnableA  = 0x24 # Debounce enable register - I/O[7-0] (Bank A) 0000 0000
SX_RegKeyConfig1       = 0x25 # Key scan configuration register 0000 0000
SX_RegKeyConfig2       = 0x26 # Key scan configuration register 0000 0000
SX_RegKeyData1         = 0x27 # Key value (column) 1111 1111
SX_RegKeyData2         = 0x28 # Key value (row) 1111 1111 
#
# LED Driver (PWM, blinking, breathing)
SX_RegTOn0             = 0x29 # ON time register for I/O[0] 0000 0000
SX_RegIOn0             = 0x2A # ON intensity register for I/O[0] 1111 1111
SX_RegOff0             = 0x2B # OFF time/intensity register for I/O[0] 0000 0000
SX_RegTOn1             = 0x2C # ON time register for I/O[1] 0000 0000
SX_RegIOn1             = 0x2D # ON intensity register for I/O[1] 1111 1111
SX_RegOff1             = 0x2E # OFF time/intensity register for I/O[1] 0000 0000
SX_RegTOn2             = 0x2F # ON time register for I/O[2] 0000 0000
SX_RegIOn2             = 0x30 # ON intensity register for I/O[2] 1111 1111
SX_RegOff2             = 0x31 # OFF time/intensity register for I/O[2] 0000 0000
SX_RegTOn3             = 0x32 # ON time register for I/O[3] 0000 0000
SX_RegIOn3             = 0x33 # ON intensity register for I/O[3] 1111 1111
SX_RegOff3             = 0x34 # OFF time/intensity register for I/O[3] 0000 0000
SX_RegTOn4             = 0x35 # ON time register for I/O[4] 0000 0000
SX_RegIOn4             = 0x36 # ON intensity register for I/O[4] 1111 1111
SX_RegOff4             = 0x37 # OFF time/intensity register for I/O[4] 0000 0000
SX_RegTRise4           = 0x38 # Fade in register for I/O[4] 0000 0000 
SX_RegTFall4           = 0x39 # Fade out register for I/O[4] 0000 0000
SX_RegTOn5             = 0x3A # ON time register for I/O[5] 0000 0000
SX_RegIOn5             = 0x3B # ON intensity register for I/O[5] 1111 1111
SX_RegOff5             = 0x3C # OFF time/intensity register for I/O[5] 0000 0000
SX_RegTRise5           = 0x3D # Fade in register for I/O[5] 0000 0000
SX_RegTFall5           = 0x3E # Fade out register for I/O[5] 0000 0000
SX_RegTOn6             = 0x3F # ON time register for I/O[6] 0000 0000
SX_RegIOn6             = 0x40 # ON intensity register for I/O[6] 1111 1111
SX_RegOff6             = 0x41 # OFF time/intensity register for I/O[6] 0000 0000
SX_RegTRise6           = 0x42 # Fade in register for I/O[6] 0000 0000
SX_RegTFall6           = 0x43 # Fade out register for I/O[6] 0000 0000
SX_RegTOn7             = 0x44 # ON time register for I/O[7] 0000 0000
SX_RegIOn7             = 0x45 # ON intensity register for I/O[7] 1111 1111
SX_RegOff7             = 0x46 # OFF time/intensity register for I/O[7] 0000 0000
SX_RegTRise7           = 0x47 # Fade in register for I/O[7] 0000 0000
SX_RegTFall7           = 0x48 # Fade out register for I/O[7] 0000 0000
SX_RegTOn8             = 0x49 # ON time register for I/O[8] 0000 0000
SX_RegIOn8             = 0x4A # ON intensity register for I/O[8] 1111 1111
SX_RegOff8             = 0x4B # OFF time/intensity register for I/O[8] 0000 0000
SX_RegTOn9             = 0x4C # ON time register for I/O[9] 0000 0000
SX_RegIOn9             = 0x4D # ON intensity register for I/O[9] 1111 1111
SX_RegOff9             = 0x4E # OFF time/intensity register for I/O[9] 0000 0000
SX_RegTOn10            = 0x4F # ON time register for I/O[10] 0000 0000
SX_RegIOn10            = 0x50 # ON intensity register for I/O[10] 1111 1111
SX_RegOff10            = 0x51 # OFF time/intensity register for I/O[10] 0000 0000
SX_RegTOn11            = 0x52 # ON time register for I/O[11] 0000 0000
SX_RegIOn11            = 0x53 # ON intensity register for I/O[11] 1111 1111
SX_RegOff11            = 0x54 # OFF time/intensity register for I/O[11] 0000 0000
SX_RegTOn12            = 0x55 # ON time register for I/O[12] 0000 0000
SX_RegIOn12            = 0x56 # ON intensity register for I/O[12] 1111 1111
SX_RegOff12            = 0x57 # OFF time/intensity register for I/O[12] 0000 0000
SX_RegTRise12          = 0x58 # Fade in register for I/O[12] 0000 0000
SX_RegTFall12          = 0x59 # Fade out register for I/O[12] 0000 0000
SX_RegTOn13            = 0x5A # ON time register for I/O[13] 0000 0000
SX_RegIOn13            = 0x5B # ON intensity register for I/O[13] 1111 1111 
SX_RegOff13            = 0x5C # OFF time/intensity register for I/O[13] 0000 0000
SX_RegTRise13          = 0x5D # Fade in register for I/O[13] 0000 0000
SX_RegTFall13          = 0x5E # Fade out register for I/O[13] 0000 0000
SX_RegTOn14            = 0x5F # ON time register for I/O[14] 0000 0000
SX_RegIOn14            = 0x60 # ON intensity register for I/O[14] 1111 1111
SX_RegOff14            = 0x61 # OFF time/intensity register for I/O[14] 0000 0000
SX_RegTRise14          = 0x62 # Fade in register for I/O[14] 0000 0000
SX_RegTFall14          = 0x63 # Fade out register for I/O[14] 0000 0000
SX_RegTOn15            = 0x64 # ON time register for I/O[15] 0000 0000
SX_RegIOn15            = 0x65 # ON intensity register for I/O[15] 1111 1111
SX_RegOff15            = 0x66 # OFF time/intensity register for I/O[15] 0000 0000
SX_RegTRise15          = 0x67 # Fade in register for I/O[15] 0000 0000
SX_RegTFall15          = 0x68 # Fade out register for I/O[15] 0000 0000 
#
# Miscellaneous
SX_RegHighInputB       = 0x69 # High input enable register - I/O[15-8] (Bank B) 0000 0000
SX_RegHighInputA       = 0x6A # High input enable register - I/O[7-0] (Bank A) 0000 0000
#
# Software Reset 
SX_RegReset            = 0x7D # Software reset register
#
# Test (not to be written) 
SX_RegTest1            = 0x7E # Test register 0000 0000
SX_RegTest2            = 0x7F # Test register

class SX1509:    
    
    def __init__(self,i2c_addr):
        '''Create an SX1509 object.
        
        Args:
            i2c_addr (int): the chip's I2C address
        '''
        
        self._i2c_addr = i2c_addr
        import smbus
        self._bus = smbus.SMBus(1)                     
    
    def set_clock(self,internal_oscillator=True,oscio_pin_is_output=False,oscio_pin_output_freq=0):
        if internal_oscillator:
            self.write_register(SX_RegClock,0b01000000)
            return
        raise Exception('Implement me')
                
    def reset(self):
        '''Reset the chip.
        
        Returns all registers to their default values.
        '''
        
        # Reset sequence (section 4.4.2)
        self.write_register(SX_RegReset,0x12)
        self.write_register(SX_RegReset,0x34)
        
    def read_register(self,addr):
        '''Read a register from the chip.
        
        Args:
            addr (int): the chip register
            
        Returns:
            int: the value of the register
        '''
        
        return self._bus.read_byte_data(self._i2c_addr,addr)
    
    def write_register(self,addr,value):
        '''Write a value to a register on the chip.
        
        Args:
            addr (int): the chip register
            value (int): the value to write to the register        
        '''
        self._bus.write_byte_data(self._i2c_addr,addr,value)        
    
    def get_ios_a(self):
        return self.read_register(SX_RegDataA)
    def get_ios_b(self):
        return self.read_register(SX_RegDataB)
        
    def set_ios_a(self,values):
        self.write_register(SX_RegDataA,values)
    def set_ios_b(self,values):
        self.write_register(SX_RegDataB,values)   
    
    # read/write pairs, individuals, bits
    
    def set_dirs_a(self,dirs):
        self.write_register(SX_RegDirA,dirs)
    def set_dirs_b(self,dirs):
        self.write_register(SX_RegDirB,dirs)
        
    def set_pull_ups_a(self,pull_ups):
        self.write_register(SX_RegPullUpA,pull_ups)
    def set_pull_ups_b(self,pull_ups):
        self.write_register(SX_RegPullUpB,pull_ups)
    
    def set_open_drains_a(self,open_drains):
        self.write_register(SX_RegOpenDrainA,open_drains)
    def set_open_drains_b(self,open_drains):
        self.write_register(SX_RegOpenDrainB,open_drains)
        
    def configure_keyboard_scan(self,num_rows,num_cols):
        if num_rows<2 or num_rows>8 or num_cols<1 or num_cols>8:
            raise Exception('Invalid rows or columns')
        v = ((num_rows-1)<<3) | (num_cols-1)
        print(v)
        self.write_register(SX_RegKeyConfig2,v)
        
    def get_keyboard_col_row(self):
        col = self.read_register(SX_RegKeyData1)
        row = self.read_register(SX_RegKeyData2)
        return col,row    
                   
    # input, slew,pullUp,PullDown,OpenDrain,Polarity,Dir,Data,InterruptMask,SenseHigh,SenseLow,InterruptSource,EventStatus,LevelShifter
    # HighInput    
    # RegClock
    # LEDDriverEnable
    # Debounce and keypad engine
    # LEDDriver(TOn0,IOn0,Off0,TOn1,IOn1,Off1,  TRise, TFall    

if __name__ == '__main__':
    
    import time
    
    exp = SX1509(0x3F)   
    exp.reset()
    time.sleep(0.1)
    
    # Needed by the keyscan engine and LED driver
    exp.set_clock(internal_oscillator=True)  
    
    # Rows (outputs)
    exp.set_dirs_a(0b11110000)        # Lower 4 pins are outputs
    exp.set_open_drains_a(0b00001111) # Lower 4 pins are open-drain
    
    # Columns (inputs)
    exp.set_dirs_b(0b11110111)     # All inputs except for LED
    exp.set_pull_ups_b(0b11110111) # All inputs pulled up
        
    exp.write_register(SX_RegDebounceConfig,  0b00000011)  # 4ms ...
    exp.write_register(SX_RegDebounceEnableB, 0b11110111)  # All inputs debounced   
    exp.write_register(SX_RegKeyConfig1,      0b00000100)  # 16ms ...
    
    exp.configure_keyboard_scan(num_rows=4, num_cols=3)
            
    while True:
        c,r = exp.get_keyboard_col_row()
        print('::'+str(c)+':'+str(r)+'::')
        time.sleep(1)
