import paho.mqtt.client as mqtt
import json

broker_address = "10.20.1.95"
client = mqtt.Client()
topic = "se443/midterm2"


msg =  { "StudentID":200203, "Name":"Rayan", "Surname":"Taha Almudawah", "Telephone":"0564086839", "Grade":95}

y = json.dumps(msg)

message = y

if (client.connect(broker_address,1883,60) ==0):
	print ("Connected succesfully to "+broker_address)
	
client.publish(topic, message)
print ("Published in "+topic+", msg = "+message)
client.disconnect();
