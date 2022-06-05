import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)

while(True): 
    time.sleep(.1)

    print("Press: Up")
    keyboard.press(Key.up)
    keyboard.release(Key.up)

    print("Press: R")
    keyboard.press('r')
    keyboard.release('r')