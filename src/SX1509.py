  
# Device and IO Banks
RegInputDisableB    = 0x00 # Input buffer disable register - I/O[15-8] (Bank B) 0000 0000
RegInputDisableA    = 0x01 # Input buffer disable register - I/O[7-0] (Bank A) 0000 0000
RegLongSlewB        = 0x02 # Output buffer long slew register - I/O[15-8] (Bank B) 0000 0000
RegLongSlewA        = 0x03 # Output buffer long slew register - I/O[7-0] (Bank A) 0000 0000
RegLowDriveB        = 0x04 # Output buffer low drive register - I/O[15-8] (Bank B) 0000 0000
RegLowDriveA        = 0x05 # Output buffer low drive register - I/O[7-0] (Bank A) 0000 0000
RegPullUpB          = 0x06 # Pull-up register - I/O[15-8] (Bank B) 0000 0000
RegPullUpA          = 0x07 # Pull-up register - I/O[7-0] (Bank A) 0000 0000
RegPullDownB        = 0x08 # Pull-down register - I/O[15-8] (Bank B) 0000 0000
RegPullDownA        = 0x09 # Pull-down register - I/O[7-0] (Bank A) 0000 0000
RegOpenDrainB       = 0x0A # Open drain register - I/O[15-8] (Bank B) 0000 0000
RegOpenDrainA       = 0x0B # Open drain register - I/O[7-0] (Bank A) 0000 0000
RegPolarityB        = 0x0C # Polarity register - I/O[15-8] (Bank B) 0000 0000
RegPolarityA        = 0x0D # Polarity register - I/O[7-0] (Bank A) 0000 0000
RegDirB             = 0x0E # Direction register - I/O[15-8] (Bank B) 1111 1111
RegDirA             = 0x0F # Direction register - I/O[7-0] (Bank A) 1111 1111
RegDataB            = 0x10 # Data register - I/O[15-8] (Bank B) 1111 1111*
RegDataA            = 0x11 # Data register - I/O[7-0] (Bank A) 1111 1111*
RegInterruptMaskB   = 0x12 # Interrupt mask register - I/O[15-8] (Bank B) 1111 1111
RegInterruptMaskA   = 0x13 # Interrupt mask register - I/O[7-0] (Bank A) 1111 1111
RegSenseHighB       = 0x14 # Sense register for I/O[15:12] 0000 0000
RegSenseLowB        = 0x15 # Sense register for I/O[11:8] 0000 0000
RegSenseHighA       = 0x16 # Sense register for I/O[7:4] 0000 0000
RegSenseLowA        = 0x17 # Sense register for I/O[3:0] 0000 0000
RegInterruptSourceB = 0x18 # Interrupt source register - I/O[15-8] (Bank B) 0000 0000
RegInterruptSourceA = 0x19 # Interrupt source register - I/O[7-0] (Bank A) 0000 0000
RegEventStatusB     = 0x1A # Event status register - I/O[15-8] (Bank B) 0000 0000
RegEventStatusA     = 0x1B # Event status register - I/O[7-0] (Bank A) 0000 0000
RegLevelShifter1    = 0x1C # Level shifter register 0000 0000
RegLevelShifter2    = 0x1D # Level shifter register 0000 0000
RegClock            = 0x1E # Clock management register 0000 0000
RegMisc             = 0x1F # Miscellaneous device settings register 0000 0000
RegLEDDriverEnableB = 0x20 # LED driver enable register - I/O[15-8] (Bank B) 0000 0000
RegLEDDriverEnableA = 0x21 # LED driver enable register - I/O[7-0] (Bank A) 0000 0000
# 
# Debounce and Keypad Engine
RegDebounceConfig   = 0x22 # Debounce configuration register 0000 0000
RegDebounceEnableB  = 0x23 # Debounce enable register - I/O[15-8] (Bank B) 0000 0000
RegDebounceEnableA  = 0x24 # Debounce enable register - I/O[7-0] (Bank A) 0000 0000
RegKeyConfig1       = 0x25 # Key scan configuration register 0000 0000
RegKeyConfig2       = 0x26 # Key scan configuration register 0000 0000
RegKeyData1         = 0x27 # Key value (column) 1111 1111
RegKeyData2         = 0x28 # Key value (row) 1111 1111 
#
# LED Driver (PWM, blinking, breathing)
RegTOn0             = 0x29 # ON time register for I/O[0] 0000 0000
RegIOn0             = 0x2A # ON intensity register for I/O[0] 1111 1111
RegOff0             = 0x2B # OFF time/intensity register for I/O[0] 0000 0000
RegTOn1             = 0x2C # ON time register for I/O[1] 0000 0000
RegIOn1             = 0x2D # ON intensity register for I/O[1] 1111 1111
RegOff1             = 0x2E # OFF time/intensity register for I/O[1] 0000 0000
RegTOn2             = 0x2F # ON time register for I/O[2] 0000 0000
RegIOn2             = 0x30 # ON intensity register for I/O[2] 1111 1111
RegOff2             = 0x31 # OFF time/intensity register for I/O[2] 0000 0000
RegTOn3             = 0x32 # ON time register for I/O[3] 0000 0000
RegIOn3             = 0x33 # ON intensity register for I/O[3] 1111 1111
RegOff3             = 0x34 # OFF time/intensity register for I/O[3] 0000 0000
RegTOn4             = 0x35 # ON time register for I/O[4] 0000 0000
RegIOn4             = 0x36 # ON intensity register for I/O[4] 1111 1111
RegOff4             = 0x37 # OFF time/intensity register for I/O[4] 0000 0000
RegTRise4           = 0x38 # Fade in register for I/O[4] 0000 0000 
RegTFall4           = 0x39 # Fade out register for I/O[4] 0000 0000
RegTOn5             = 0x3A # ON time register for I/O[5] 0000 0000
RegIOn5             = 0x3B # ON intensity register for I/O[5] 1111 1111
RegOff5             = 0x3C # OFF time/intensity register for I/O[5] 0000 0000
RegTRise5           = 0x3D # Fade in register for I/O[5] 0000 0000
RegTFall5           = 0x3E # Fade out register for I/O[5] 0000 0000
RegTOn6             = 0x3F # ON time register for I/O[6] 0000 0000
RegIOn6             = 0x40 # ON intensity register for I/O[6] 1111 1111
RegOff6             = 0x41 # OFF time/intensity register for I/O[6] 0000 0000
RegTRise6           = 0x42 # Fade in register for I/O[6] 0000 0000
RegTFall6           = 0x43 # Fade out register for I/O[6] 0000 0000
RegTOn7             = 0x44 # ON time register for I/O[7] 0000 0000
RegIOn7             = 0x45 # ON intensity register for I/O[7] 1111 1111
RegOff7             = 0x46 # OFF time/intensity register for I/O[7] 0000 0000
RegTRise7           = 0x47 # Fade in register for I/O[7] 0000 0000
RegTFall7           = 0x48 # Fade out register for I/O[7] 0000 0000
RegTOn8             = 0x49 # ON time register for I/O[8] 0000 0000
RegIOn8             = 0x4A # ON intensity register for I/O[8] 1111 1111
RegOff8             = 0x4B # OFF time/intensity register for I/O[8] 0000 0000
RegTOn9             = 0x4C # ON time register for I/O[9] 0000 0000
RegIOn9             = 0x4D # ON intensity register for I/O[9] 1111 1111
RegOff9             = 0x4E # OFF time/intensity register for I/O[9] 0000 0000
RegTOn10            = 0x4F # ON time register for I/O[10] 0000 0000
RegIOn10            = 0x50 # ON intensity register for I/O[10] 1111 1111
RegOff10            = 0x51 # OFF time/intensity register for I/O[10] 0000 0000
RegTOn11            = 0x52 # ON time register for I/O[11] 0000 0000
RegIOn11            = 0x53 # ON intensity register for I/O[11] 1111 1111
RegOff11            = 0x54 # OFF time/intensity register for I/O[11] 0000 0000
RegTOn12            = 0x55 # ON time register for I/O[12] 0000 0000
RegIOn12            = 0x56 # ON intensity register for I/O[12] 1111 1111
RegOff12            = 0x57 # OFF time/intensity register for I/O[12] 0000 0000
RegTRise12          = 0x58 # Fade in register for I/O[12] 0000 0000
RegTFall12          = 0x59 # Fade out register for I/O[12] 0000 0000
RegTOn13            = 0x5A # ON time register for I/O[13] 0000 0000
RegIOn13            = 0x5B # ON intensity register for I/O[13] 1111 1111 
RegOff13            = 0x5C # OFF time/intensity register for I/O[13] 0000 0000
RegTRise13          = 0x5D # Fade in register for I/O[13] 0000 0000
RegTFall13          = 0x5E # Fade out register for I/O[13] 0000 0000
RegTOn14            = 0x5F # ON time register for I/O[14] 0000 0000
RegIOn14            = 0x60 # ON intensity register for I/O[14] 1111 1111
RegOff14            = 0x61 # OFF time/intensity register for I/O[14] 0000 0000
RegTRise14          = 0x62 # Fade in register for I/O[14] 0000 0000
RegTFall14          = 0x63 # Fade out register for I/O[14] 0000 0000
RegTOn15            = 0x64 # ON time register for I/O[15] 0000 0000
RegIOn15            = 0x65 # ON intensity register for I/O[15] 1111 1111
RegOff15            = 0x66 # OFF time/intensity register for I/O[15] 0000 0000
RegTRise15          = 0x67 # Fade in register for I/O[15] 0000 0000
RegTFall15          = 0x68 # Fade out register for I/O[15] 0000 0000 
#
# Miscellaneous
RegHighInputB       = 0x69 # High input enable register - I/O[15-8] (Bank B) 0000 0000
RegHighInputA       = 0x6A # High input enable register - I/O[7-0] (Bank A) 0000 0000
#
# Software Reset 
RegReset            = 0x7D # Software reset register
#
# Test (not to be written) 
RegTest1            = 0x7E # Test register 0000 0000
RegTest2            = 0x7F # Test register

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
            self.write_register(RegClock,0b01000000)
            return
        raise Exception('Implement me')
                
    def reset(self):
        '''Reset the chip.
        
        Returns all registers to their default values.
        '''
        
        # Reset sequence (section 4.4.2)
        self.write_register(RegReset,0x12)
        self.write_register(RegReset,0x34)
        
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
        return self.read_register(RegDataA)
    def get_ios_b(self):
        return self.read_register(RegDataB)
        
    def set_ios_a(self,values):
        self.write_register(RegDataA,values)
    def set_ios_b(self,values):
        self.write_register(RegDataB,values)   
    
    # read/write pairs, individuals, bits
    
    def set_dirs_a(self,dirs):
        self.write_register(RegDirA,dirs)
    def set_dirs_b(self,dirs):
        self.write_register(RegDirB,dirs)
        
    def set_pull_ups_a(self,pull_ups):
        self.write_register(RegPullUpA,pull_ups)
    def set_pull_ups_b(self,pull_ups):
        self.write_register(RegPullUpB,pull_ups)
    
    def set_open_drains_a(self,open_drains):
        self.write_register(RegOpenDrainA,open_drains)
    def set_open_drains_b(self,open_drains):
        self.write_register(RegOpenDrainB,open_drains)
        
    def configure_keyboard_scan(self,num_rows,num_cols):
        if num_rows<2 or num_rows>8 or num_cols<1 or num_cols>8:
            raise Exception('Invalid rows or columns')
        v = ((num_rows-1)<<3) | (num_cols-1)
        self.write_register(RegKeyConfig2,v)
        
    def get_keyboard_row_col(self):
        col = self.read_register(RegKeyData1)
        row = self.read_register(RegKeyData2)
        colcnt = 0        
        if col != 255:
            colcnt += 1
            while (col & 1) == 1:                
                col = col >> 1
                colcnt += 1
        rowcnt = 0
        if row != 255:
            rowcnt += 1
            while (row & 1) == 1:
                row = row >> 1
                rowcnt += 1                
        return rowcnt,colcnt   
                   
    # input, slew,pullUp,PullDown,OpenDrain,Polarity,Dir,Data,InterruptMask,SenseHigh,SenseLow,InterruptSource,EventStatus,LevelShifter
    # HighInput    
    # RegClock
    # LEDDriverEnable
    # Debounce and keypad engine
    # LEDDriver(TOn0,IOn0,Off0,TOn1,IOn1,Off1,  TRise, TFall    
  
    