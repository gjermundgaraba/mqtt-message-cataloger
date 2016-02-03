import paho.mqtt.client as mqtt
import configparser
import json
from pymongo import MongoClient

config = configparser.ConfigParser()
config.read('config.ini')

mqtt_host = config['MQTTSERVER']['Host']
mqtt_port = int(config['MQTTSERVER']['Port'])
mqtt_keep_alive = int(config['MQTTSERVER']['Keep_Alive'])
mqtt_topics = json.loads(config["MQTTSERVER"]["Topics"])

mongo_host = config['MONGO']['Host']
mongo_port = int(config['MONGO']['Port'])
mongo_database_name = config['MONGO']['Database']
mongo_collection_name = config['MONGO']['Collection']

mongo_client = MongoClient(mongo_host, mongo_port)
mongo_database = mongo_client[mongo_database_name]
mongo_collection = mongo_database[mongo_collection_name]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in mqtt_topics:
        client.subscribe(topic)

def on_message(client, userdata, message):
    decoded_message = message.payload.decode("utf-8")
    database_record = {
        "topic": message.topic,
        "message": decoded_message
    }
    mongo_collection.insert_one(database_record)
    print("Received message '" + decoded_message + "' on topic '" + message.topic + "' with QoS " + str(message.qos))


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(mqtt_host, mqtt_port, mqtt_keep_alive)

mqtt_client.loop_forever()
