import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

# Define the relay pin number
relay_pin = 38

# Setup the GPIO pin for the relay
gpio.setup(relay_pin, gpio.OUT, initial=gpio.LOW)

try:
    # Turn on the relay
    gpio.output(relay_pin, True)
    print("Relay is Switched On. Please press Ctrl+C to exit.")
    
    # Wait for 15 seconds
    time.sleep(15)
    
    # Turn off the relay
    print("Relay is Switched off.")
    gpio.output(relay_pin, False)

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    gpio.cleanup()
    print("Program Exited")


'''
1.	copy path of p4
2.	Open Terminal
3.	Run  "crontab -e"
4.	go to down
5.	Replace /path/to/your/program with the actual directory path.
6.	Update time
7.	Press Ctrl + X, then Y, and Enter
8.	Program will run on given time
'''