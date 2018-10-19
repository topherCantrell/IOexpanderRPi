import time

def set_line_input(x):
    # Pull down resistor
    # TODO I2C communication here
    pass
    
def set_line_output(x):
    # Drive line high
    # TODO I2C communication here
    pass

def is_line_high(x):
    # Return true if line is high
    # TODO I2C communication here
    return False

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
    
for x in range(32):
    set_line_input(x)
    
while True:
    sweep()
