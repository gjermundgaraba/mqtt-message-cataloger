import configparser
import json


class MmcConfiguration:
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
