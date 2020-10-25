from threading import *
import time

class PrintMessage(Thread):
    lock=Lock()

    def __init__(self,message):
        Thread.__init__(self)
        self.message=message
    def run(self):
        for i in range(5):
            print(str(i)+" time "+self.message)
            time.sleep(1)



startTime=time.perf_counter()
messages=["Hello","HI"]
objs=[PrintMessage(i) for i in messages]
for obj in objs:
    obj.start()
for obj in objs:
    obj.join()


endTime=time.perf_counter()

print("Time Taken to complete "+str((int)(endTime-startTime))+"s")