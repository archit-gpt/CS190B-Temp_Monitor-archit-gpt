import json, subprocess, time
import RPi.GPIO as GPIO
import Adafruit_DHT
from datetime import datetime
import firebase
from watchdog import Watchdog


# setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
MAX_TEMP = 4
MIN_TEMP = 1

# firebase code
firebase.database()
firebase.storage()

# reference to database service
db = firebase.database()


# send text-- this code is from ClickSend The Blog
username 	= 'erindelong@ucsb.edu'									# Your ClickSend username
api_key 	= '70C38ED1-217F-6B9F-8EE3-4ECB5DD87313'	# Your Secure Unique API key
msg_to 		= '+19259898099'						# Recipient Mobile Number in international format (+61411111111 test number).
msg_from 	= ''								# Custom sender ID (leave blank to accept replies).
msg_body    = ''

def send_text(username, api_key, msg_to, msg_from, msg_body):
    request = { "messages" : [ { "source":"rpi", "from":msg_from, "to":msg_to, "body":msg_body } ] }
    request = json.dumps(request)
    cmd = "curl https://rest.clicksend.com/v3/sms/send -u " + username + ":" + api_key + " -H \"Content-Type: application/json\" -X POST --data-raw '" + request + "'"
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    (output,err) = p.communicate()

def loop(file):
    while True:
        try:
            with Watchdog(10):
                humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
                current_time = datetime.today().strftime(': %Y-%m-%d %H:%M:%S')+"\n"
                if humidity is not None and temperature is not None:
                    print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                    file.write("Temp={0:0.1f}*C%".format(temperature))
                    if (temperature > MAX_TEMP):
                        msg_body = "The temperature in your fridge is too high: " + str(temperature) + " degrees Celsius"
                        send_text(username, api_key, msg_to, msg_from, msg_body)
                    elif (temperature < MIN_TEMP):
                        msg_body = "The temperature in your fridge is too low: " + str(temperature) + " degrees Celsius"
                        send_text(username, api_key, msg_to, msg_from, msg_body)
                    db.child("pi").child("data").update({"temperature": temperature, "humidity": humidity})
                else:
                    print("Sensor failed.")
                    file.write("Sensor failed")
                file.write(current_time)
                time.sleep(5)
        except Watchdog:
            print("Code took too long to execute-- watchdog")
            file.write("Code took too long to execute-- watchdog\n")
            file.close()

if __name__ == "__main__":
    file = open("logging_file.txt","a")
    loop(file)

