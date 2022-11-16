import time
import paho.mqtt.client as paho
import json

broker = "10.20.1.95"

def on_message(client, userdata, message):
    time.sleep(1)
    msg = json.loads(str(message.payload.decode("utf-8")))

    print("msg['StudentID']=", msg["StudentID"]) 
    print("msg['Name']=", msg["Name"]) 
    print("msg['Surname']=", msg["Surname"]) 
    print("msg['Telephone']=", msg["Telephone"]) 
    print("msg['Grade']=", msg["Grade"]) 
 
    

client= paho.Client() 
client.on_message = on_message
print("connecting to broker ",broker)


client.connect(broker)
client.loop_start()
print("subscribing ")


client.subscribe("se443/midterm2")
while(True):
	client.on_message=on_message
