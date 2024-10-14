import gpiod
import time

chip=gpiod.Chip("gpiochip4")
pirLine=chip.get_line(22)
pirLine.request(consumer="PIR Sensor",type=gpiod.LINE_REQ_DIR_IN)
ledLine=chip.get_line(17)
ledLine.request(consumer="Led Light",type=gpiod.LINE_REQ_DIR_OUT)

try:
    ind=1
    for i in range(15):
        if(pirLine.get_value()==1) and ind%2==1:
            ledLine.set_value(1)
            time.sleep(2)            
            ledLine.set_value(0)
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    pirLine.release()
    ledLine.release()
    print("Line Released")