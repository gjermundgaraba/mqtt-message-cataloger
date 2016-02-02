import paho.mqtt.client as mqtt
import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')

host = config['MQTTSERVER']['Host']
port = int(config['MQTTSERVER']['Port'])
keep_alive = int(config['MQTTSERVER']['Keep_Alive'])
topics = json.loads(config["MQTTSERVER"]["Topics"])


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in topics:
        client.subscribe(topic)



def on_message(client, userdata, message):
    decoded_message = message.payload.decode("utf-8")
    print("Received message '" + decoded_message + "' on topic '" + message.topic + "' with QoS " + str(message.qos))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, keep_alive)

client.loop_forever()
