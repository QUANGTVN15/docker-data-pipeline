import requests
from kafka import KafkaProducer
import json
import os
import time

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL", "broker:9092")
TOPIC_NAME = os.environ.get("TOPIC_NAME", "joke")
SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        joke_type = data.get('type')
        if joke_type == 'single':
            joke_text = data.get('joke', '')
            joke_setup = None
            joke_delivery = None
        else:
            joke_text = None
            joke_setup = data.get('setup', '')
            joke_delivery = data.get('delivery', '')
        return {
            "id": int(data.get('id', -1)),
            "category": data.get('category'),
            "type": joke_type,
            "joke": joke_text,
            "setup": joke_setup,
            "delivery": joke_delivery,
            "lang": data.get('lang'),
            "flags": data.get('flags')
        }
    else:
        return None

def run():
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BROKER_URL],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    iterator = 0
    while True:
        joke = get_joke()
        if joke:
            print(f"Sending joke #{iterator}: {joke}")
            producer.send(TOPIC_NAME, value=joke)
            producer.flush()
        else:
            print("No joke fetched!")
        time.sleep(SLEEP_TIME)
        iterator += 1

if __name__ == "__main__":
    run()
