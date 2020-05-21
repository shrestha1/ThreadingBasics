import threading
# import queue
import numpy as np
import time

"""
event.set() to set the flag true
event.clear() to set the flag false
event.wait() to block until event.set() is true
event.is_set() to check if the event.set() is true
"""
# print(dir(threading))

def flag():
    time.sleep(3)

    event.set()
    print("starting countdown")
    time.sleep(7)
    print("event is cleared")
    event.clear()

def start_operations():
    event.wait()
    while event.is_set():
        print("starting random integer task")
        x = np.random.randint(1,30)
        time.sleep(.5)
        if x == 29 :
            print(True)

    print("Event has been vcleared")

event = threading.Event()

t1 = threading.Thread(target= flag)
t2 = threading.Thread(target= start_operations)


t1.start()
t2.start()