#!/usr/bin/env python

import paho.mqtt.client as mqtt
import time
import copy

userdata = {}

def updateScreen(userdata) : 
    print ("Request screen update")

# Definition du comportement en cas de reception d'un evenement
def on_message(client, userdata, message):
    print("message received  ",str(message.payload.decode("utf-8")),\
        "topic",message.topic,"retained ",message.retain)
    if message.retain==1:
        print("This is a retained message")
    current_temperature = message.payload.decode("utf-8")
    if not userdata.has_key(message.topic) :
        userdata[message.topic] = current_temperature
        updateScreen(userdata)       
    else :
        if userdata[message.topic] != current_temperature : 
            userdata[message.topic] = current_temperature
            updateScreen(userdata)

    return


# Creation du client pour se connecter
broker_address = "localhost"
broker_port = "1883"
sensor_topic="prometheus/#"

clientMqtt = mqtt.Client("sensors", userdata=userdata)
clientMqtt.on_message = on_message
clientMqtt.connect(broker_address)
clientMqtt.subscribe(sensor_topic)


while True : 
    clientMqtt.loop_start()
    time.sleep(1)



