import machine
import time
#print("test")
#pin2 = machine.Pin(2,machine.Pin.OUT)
#print(pin2.value())

def blink_led2():
  pin = machine.Pin(2,machine.Pin.OUT)
  for i in range (10):
    print("Blink 10 times this is blink no"+i)
    time.sleep(1)
    pin.value(i%2)

blink_led2()
