# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony Dicola, Justin Cooper

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, Data, RequestError
import datetime
import time
import json
from sense_hat import SenseHat
sense = SenseHat()
temp = sense.temp

leer=json.loads(open('miflora.json').read())

#print (leer)
temperatura=leer['temperature']
#print (leer['battery'])
#print (bateria)
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'f7da2166f5cb4349a0d7af9e8bd2dede'
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'fermax'



# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    temperature = aio.feeds('temperature')
except RequestError:
    feed = Feed(name="temperature")
    temperature = aio.create_feed(feed)

#
# Adding data
#

aio.send_data(temperature.key, temperatura)
# works the same as send now
aio.append(temperature.key, temperatura)

# setup batch data with custom created_at values
yesterday = (datetime.datetime.today() - datetime.timedelta(1)).isoformat()
today = datetime.datetime.now().isoformat()
data_list = [Data(value=50, created_at=today), Data(value=33, created_at=yesterday)]
# send batch data
aio.send_batch_data(temperature.key, data_list)

#
# Retrieving data
#


#for number in range(3):
data = aio.receive(temperature.key)
print(data)


