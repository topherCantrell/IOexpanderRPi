
KEY_ROW_1 = 0 #  --1 2 3    Board pin 2
KEY_ROW_2 = 3 #  --4 5 6    Board pin 7 (far right)         
KEY_ROW_3 = 2 #  --7 8 9    Board pin 6              
KEY_ROW_4 = 1 #  --# 0 *    Board pin 4
#                  | | |
KEY_COL_1 = 9  # --+ | |    Board pin 3
KEY_COL_2 = 8  # ----+ |    Board pin 1 (far left)
KEY_COL_3 = 10 # ------+    Board pin 5

import time
import SX1509 as SX

io = SX.SX1509(0x3F)
io.reset()
time.sleep(0.1)
    
# Needed by the keyscan engine and LED driver
io.set_clock(internal_oscillator=True)  

# Rows (outputs)
io.set_dirs_a(0b11110000)        # Lower 4 pins are outputs
io.set_open_drains_a(0b00001111) # Lower 4 pins are open-drain

# Columns (inputs)
io.set_dirs_b(0b11110111)     # All inputs except for LED
io.set_pull_ups_b(0b11110111) # All inputs pulled up
    
io.write_register(SX.RegDebounceConfig,  0b00000011)  # 4ms ...
io.write_register(SX.RegDebounceEnableB, 0b11110111)  # All inputs debounced   
io.write_register(SX.RegKeyConfig1,      0b00000100)  # 16ms ...

io.configure_keyboard_scan(num_rows=4, num_cols=3)

KEYMAP = {
    '21' : '0',
    '12' : '1',
    '11' : '2',
    '13' : '3',
    '42' : '4',
    '41' : '5',
    '43' : '6',
    '32' : '7',
    '31' : '8',
    '33' : '9',
    '22' : '*',
    '23' : '#'
    }
        
while True:
    r,c = io.get_keyboard_row_col()    
    
    if r!=0 and c!=0:
        print("Pressed "+KEYMAP[str(r)+str(c)])        
        
    time.sleep(1)
