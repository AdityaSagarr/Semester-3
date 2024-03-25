import RPi.GPIO as gpio
from flask import Flask, render_template
import datetime

app = Flask(__name__)

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led = 11  # Pin connected to LED
switch1 = 13  # Pin connected to switch

gpio.setup(led, gpio.OUT, initial=1)
gpio.setup(switch1, gpio.IN)

light_status = "OFF"

def glow_led(event):
    print("Entered Here")
    global light_status
    if event == switch1 and light_status == "OFF":
        gpio.output(led, False)
        light_status = "ON"
    elif event == switch1 and light_status == "ON":
        gpio.output(led, True)
        light_status = "OFF"

@app.route("/")
def led_status():
    global light_status
    now = datetime.datetime.now()
    time_string = now.strftime("%H:%M %d-%m-%Y")
    template_data = {
        'status': light_status,
        'time': time_string
    }
    return render_template('lightstatus.html', **template_data)

gpio.add_event_detect(switch1, gpio.RISING, callback=glow_led, bouncetime=100)

if __name__ == "__main__":
    app.run(debug=True, port=4000, host='169.254.185.235')
