# Run different parts of a program in different times
# GIL = global interpreter lock 

# cpu bound prog or task - waiting for internal events 
# i/o bount waiting for user input waiting for external events

import threading
import time

def eatBreakfast():
    time.sleep(3)
    print("You eat breakfast")
    
def drinkCoffee():
    time.sleep(4)
    print('You drink coffee')
    
def study():
    time.sleep(5)
    print("You finished studying")

x = threading.Thread(target=eatBreakfast, args=())
x.start()

y = threading.Thread(target=drinkCoffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())