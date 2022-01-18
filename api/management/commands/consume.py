import json
from kafka import KafkaConsumer
from api.tasks import create_room,create_vehicle
from api.utils import remove_from_tmp
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start Consumer'

    def handle(self, *args, **options):
        # channel
        topic = 'app'

        # consumer

        consumer = KafkaConsumer(topic, bootstrap_servers=[
            'localhost:9092'], auto_offset_reset='latest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

        for message in consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))

            if message.key == b'create_room':
                create_room(message.value)
                remove_from_tmp(file_path=message.value['images'])
            
            if message.key == b'create_vehicle':
                create_vehicle(message.value)
                remove_from_tmp(file_path=message.value['images'])
