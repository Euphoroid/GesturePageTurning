import board
import usb_hid

from adafruit_apds9960.apds9960 import APDS9960
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

i2c = board.I2C()
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = True

kbd = Keyboard(usb_hid.devices)

while True:
    gesture = apds.gesture()
    if gesture == 0x01:
        print("next")
        kbd.send(Keycode.LEFT_ARROW)
    elif gesture == 0x02:
        print("prev")
        kbd.send(Keycode.RIGHT_ARROW)
    elif gesture == 0x04:
        print("refresh")
        kbd.send(Keycode.F4)
