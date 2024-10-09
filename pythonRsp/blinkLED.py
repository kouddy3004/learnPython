import gpiod
import time
ledPin = {0:27,1:17}
chip = gpiod.Chip('gpiochip4')
led_line=None

def powerOnLed(index):
    led_line = chip.get_line(ledPin[index])
    led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
    led_line.set_value(1)
    time.sleep(1)
    led_line.set_value(0)
    time.sleep(1)
    if led_line is not None:
        led_line.release()
        
def powerOnLeds(index):
    led_line = chip.get_line(ledPin[0])
    led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
    led_line1 = chip.get_line(ledPin[1])
    led_line1.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
    led_line.set_value(1)
    led_line1.set_value(1)
    time.sleep(1)
    led_line.set_value(0)
    led_line1.set_value(0)
    time.sleep(1)
    if led_line is not None:
        led_line.release()
    if led_line1 is not None:
        led_line1.release()
        
try:
    for i in range(4):
        powerOnLed(i%2)
    powerOnLeds(i%2)
        
finally:
    if led_line is not None:
        led_line.release()
