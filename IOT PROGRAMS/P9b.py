# 9b
import socket
import RPi.GPIO as GPIO
import time

Buzzer = 36
HOST = '169.254.185.235'  # The server's hostname or IP address
PORT = 5000  # The port used by the server

GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.OUT)
GPIO.setwarnings(False)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            data = s.recv(1024).decode('utf-8')
            print(data)
            if str(data) == 'Alert':
                print("Alert! Gas Leakage detected")
                GPIO.output(36, True)
                time.sleep(3)
                GPIO.output(36, False)
                time.sleep(3)
except KeyboardInterrupt:
    s.close()
    GPIO.cleanup()