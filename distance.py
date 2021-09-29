import time
import RPi.GPIO as GPIO
import explorerhat

def main():
    CS = 8
    runtime = 300.0
    uptime = 0.000020
    interval = 0.020000
    GPIO.setup(CS, GPIO.OUT)
    explorerhat.analog.one.changed(lambda self, value: print(value, time.time()))
    now = start = time.time()
    while now - start < runtime:
        GPIO.output(CS, True)
        time.sleep(uptime) # Ten microseconds
        GPIO.output(CS, False)
        time.sleep(interval - uptime)
        now = time.time()
    
if __name__ == "__main__":
    main()
