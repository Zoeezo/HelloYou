from microbit import *

'''
Als het donker is wordt de microbit sad
'''
while True:
    if (display.read_light_level() < 10):
        display.clear()
        display.show(Image.SAD)
    else:
        display.clear()
        display.show(Image.HAPPY)