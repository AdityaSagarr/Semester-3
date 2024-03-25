import RPi.GPIO as gpio
import picamera
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led = 15
pir = 12
HIGH = 1
LOW = 0

gpio.setup(led, gpio.OUT)  # Initialize GPIO Pin as output
gpio.setup(pir, gpio.IN)  # Initialize GPIO Pin as input

fromaddr = "your_email@gmail.com"  # change the email address accordingly
toaddr = "toaddr@gmail.com"

def sendMail(data):
    mail = MIMEMultipart()
    mail['From'] = fromaddr
    mail['To'] = toaddr
    mail['Subject'] = "Attachment"
    body = "Please find the attachment"
    mail.attach(MIMEText(body, 'plain'))

    dat = data + '.jpg'
    attachment = open(dat, "rb")
    image = MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "your_password")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def capture_image():
    data = time.strftime("Image was captured on %M:%S %d_%b_%Y")
    camera.start_preview()
    time.sleep(3)
    print(data)
    camera.capture("{}.jpg".format(data))
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)
    gpio.output(led, LOW)

camera = picamera.PiCamera()
camera.rotation = 380
camera.awb_mode = 'auto'
camera.brightness = 55

while True:
    if gpio.input(pir) == 1:
        gpio.output(led, HIGH)
        capture_image()
    while gpio.input(pir) == 1:
        time.sleep(1)
    else:
        gpio.output(led, LOW)
        time.sleep(0.01)
