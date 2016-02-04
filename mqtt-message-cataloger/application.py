import paho.mqtt.client as mqtt
from pymongo import MongoClient
from configuration import MmcConfiguration

def on_connect(client, userdata, flags, rc):
    for topic in MmcConfiguration.mqtt_topics:
        client.subscribe(topic)

def on_message(client, userdata, message):
    decoded_message = message.payload.decode("utf-8")
    database_record = {
        "topic": message.topic,
        "message": decoded_message
    }
    mongo_collection.insert_one(database_record)

mongo_client = MongoClient(MmcConfiguration.mongo_host, MmcConfiguration.mongo_port)
mongo_database = mongo_client[MmcConfiguration.mongo_database_name]
mongo_collection = mongo_database[MmcConfiguration.mongo_collection_name]

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MmcConfiguration.mqtt_host, MmcConfiguration.mqtt_port, MmcConfiguration.mqtt_keep_alive)

mqtt_client.loop_forever()
