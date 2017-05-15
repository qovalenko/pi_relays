import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

GPIO.setmode(GPIO.BCM)

MQTT_BROKER = "104.131.167.212"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "testTopic"

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

SleepTimeS = 0.2
SleepTimeL = 0.5
 
GPIO.setup(3, GPIO.OUT) 
GPIO.output(3, GPIO.HIGH)

GPIO.setup(4, GPIO.OUT) 
GPIO.output(4, GPIO.HIGH)

def on_connect(mosq, obj, rc):
  #Subscribe to a the Topic
  mqttc.subscribe(MQTT_TOPIC, 0)

# Define on_subscribe event Handler
def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to MQTT Topic")

# Define on_message event Handler
def on_message(mosq, obj, msg):
  print(msg.payload)
  GPIO.output(3, GPIO.LOW)
  time.sleep(SleepTimeS);
  GPIO.output(3, GPIO.HIGH)

  GPIO.output(4, GPIO.LOW)
  time.sleep(SleepTimeS);
  GPIO.output(4, GPIO.HIGH)


mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL )
mqttc.loop_forever()


A

