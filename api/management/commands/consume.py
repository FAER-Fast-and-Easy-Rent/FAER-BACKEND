import os
import json
from kafka import KafkaConsumer
from api.tasks import create_room, create_vehicle
from api.utils import remove_from_tmp
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start Consumer'

    def handle(self, *args, **options):
        brokers = "rocket-03.srvs.cloudkafka.com:9094,rocket-01.srvs.cloudkafka.com:9094,rocket-02.srvs.cloudkafka.com:9094"
        topic = '0iuij7z1-faer'

        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=brokers,
                                 security_protocol='SASL_SSL',
                                 sasl_mechanism='SCRAM-SHA-256',
                                 sasl_plain_username='0iuij7z1',
                                 sasl_plain_password='G7WL8CTe6_xYF-yziEHXjDaOLbsXJRHy',
                                 auto_offset_reset='latest',
                                 value_deserializer=lambda x: json.loads(x.decode('utf-8'))
                                 )

        print('Start consuming')
        print ("Is it Directory?" + str(os.path.isdir('temp')))
        print(os.listdir('temp'))
        for message in consumer:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key, message.value))

            if message.key == b'create_room':
                create_room(message.value)
                remove_from_tmp(file_path=message.value['images'])

            if message.key == b'create_vehicle':
                create_vehicle(message.value)
                remove_from_tmp(file_path=message.value['images'])
