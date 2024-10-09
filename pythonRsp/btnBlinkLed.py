import gpiod
import time
btnPin = 26
ledPin = 17
chip = gpiod.Chip('gpiochip4')
btn_line = chip.get_line(btnPin)
led_line = chip.get_line(ledPin)
btn_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
print("Execution Started")
try:
    for i in range(10):
        led_line.set_value(btn_line.get_value())
        time.sleep(2)
finally:
    btn_line.release()
    led_line.release()
    print("Line Released")

