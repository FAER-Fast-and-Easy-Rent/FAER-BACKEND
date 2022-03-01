import os
import cv2
import json
import base64
import numpy as np
import firebase_admin
from django.conf import settings
from firebase_admin import storage
from django.template import loader
from django.core.mail import EmailMultiAlternatives

credentials = {
    "type": "service_account",
    "project_id": "faer-342211",
    "private_key_id": "051db07126f93e713d03dc9106d6972ea938d1dd",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCnTf6fKSOcIXmv\nEN/ct9HiOzB1Br+bc5USWN0c8UUsPAp9a4Zj6Dgv3osBBJI3cNAerSVdagDPXbL0\nx/BNP89SsT+LTtFY0m4tFbxXL2r78j7vMMtb6lecEMV9JcVFBUe5Dqpi6vFuzds1\ncOK14ogwH/iNgO43aQ9aNi2njCt+EFHUrNKly4CxWVseRyz9xmkhrJb+9TMOWbPo\n9CpaneVRmXPrU6dF/bFrOVZ/jLiSSvdpvotyEmwaEeES+UCCUL/tb7QeXPEJ/4HU\nS/+fxDhC56fcQPd23GIEnI+ULqJBGubeB9/O6ilawQAFaUey3Ssny6E3SxojjV1Q\nIqJWImPBAgMBAAECggEAIsNciFLCgPMdtygg89pIJKNa1r4vuwvBql3Hl/d0AZR6\nM4RPmNvMLPonVO9PuHBa9jzQ+j+H6o6UHDOdNVfwasTEqNwYOMYEuZ5+E3mZV7+G\nnym6357qVFXRy0a5XjWSKRwogEREJVtl1I1fth5bYPCLs09acC4G0B5YzysbcGZ6\nrf+DpCWEoX4IH1pydG3erHiAVPv1x70ozzjQHsp0wg8+B4/Y+7IV0mZn1crCCE4D\nxoojX6R8W3Vw6MYcCpEyY9ztz/238Zt/OhsfTm/LPea9IixdfGTPG2cc6XOxwA6r\nzPBRoUOhX70fTuEatQE89NdabhUKKLOxdQSzEchSZwKBgQDShJ2gK/ewQbTJmeDf\nMUGO8861ritwLUdnJVWFe1q19DryHe+75UzJDV+tt9H/fbQ6vnxIMPG+2r2rXEqf\ndZ0wNhPSNZrLMQCIhkOpXO4ZtNhcrARbnXnuRJJbkKWH8+vrdy1CyQKnskcrOOvY\n0Va7DodZ3huvi6Bb8eh+TBbLtwKBgQDLc1LCZo4Z3bqNViR9s7KeCJ83XETfhpAt\n6EHfTGtbuLJEDNcjxmAZMFLHbcXWMKVcgmQEwC+E0giLgn6s6wb+YJ9GWJ+O66CT\neewmJJ+9KUlHlKJ4UqwgckDicTfiw3YHBIf6xhgvTPheZCCI2aY1oZpktGtCcWPS\n1fKgXnc8RwKBgQDQ92739WzyeuaYT7TWGDC5U+5WjcL0oR2Fl5ui2mWaxApXF7xG\nyUBFOo9FA3jiocbroPYBOwRcrQklNoGkc71KhAN84FT9aXDcFFrJnUOEJO24X9Ab\nmN/V0h9t4NFPeKMwoqY86wdFq0PV9bS3DmWHXM6iOEVHJdRSMHjWFXVzVQKBgHmc\nN43oS2x+szIkma9hqJT6RmGLD8gk4S3vtOBLB6lN35D5s+e4flzQG8sFfMopTc7c\nSfjlAAJ+oYjyudGWsxl+m/Yqp0WA5v0AVf3+ylUBxsG4wNz3XdgPM2Wnk2ZCu9w6\nAyYNHwu3EIcrhp8GqmlIbcdgaPTQXoD6Tgs6LD+lAoGAH254w6s8e66OTWAYURXj\nWsBfyxf641h2ZI1HENQvdfvsvmJ6x8pX4a6aYv2UqJQmf6NjUF8VbLTLEbvRwYku\nbXWBjGhxMxDIq4YSq/mJjW5n/+RkDVM1tEboVhE6qZYIv6HlZNzCEdCD+NhFbscT\nnG3rFuXxL0uktpUkkJPp7Qc=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-z6vwy@faer-342211.iam.gserviceaccount.com",
    "client_id": "109755727002122016058",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-z6vwy%40faer-342211.iam.gserviceaccount.com"
}


os.environ['FIREBASE_CRED'] = json.dumps(credentials)

service_account_info = json.loads(os.environ.get('FIREBASE_CRED', None))
cred = firebase_admin.credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred, {'storageBucket': 'faer-342211.appspot.com'})

default_img_url = 'https://storage.googleapis.com/faer-342211.appspot.com/default.jpg'


def write_to_tmp(file):
    file_path = f'temp/{file}'
    encoded_file = base64.b64encode(file.read())

    # with open(file_path, 'wb+') as f:
    #     f.write(file.read())
    print(f'File added encoded:{file_path}')
    return {
        'file_name': file,
        'encoded_file': encoded_file.decode("utf-8")
    }


def serializeImg(img):
    image = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)
    _, img_buffer_arr = cv2.imencode(".jpg", image)
    img_bytes = img_buffer_arr.tobytes()
    print(len(img_bytes))
    return img_bytes


def remove_from_tmp(file_path):
    os.remove(file_path)
    print(f'File removed :{file_path}')


def upload_to_storage(image):
    fileName = image['file_name']
    bucket = storage.bucket()
    blob = bucket.blob('faer/' + fileName)
    # blob.upload_from_filename(fileName)
    decoded_file = base64.b64decode(image['encoded_file'])
    blob.upload_from_string(decoded_file, content_type='image/png')
    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("File has been uploaded to : ", blob.public_url)
    return blob.public_url


def get_media_url(image):

    media_url = upload_to_storage(image)
    return media_url if media_url else default_img_url


def upload_to_firebase(file):
    fileName = 'random.png'
    bucket = storage.bucket()
    blob = bucket.blob('faer/' + fileName)
    blob.upload_from_string(file.read(), content_type='image/png')
    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("File has been uploaded to : ", blob.public_url)
    return blob.public_url


def send_email(sub, user, owner, product, to):
    template = loader.get_template("reservation_email.txt")
    context = {
        "renter": owner,
        "user": user,
        "product": product
    }
    message = template.render(context)
    msg = EmailMultiAlternatives(subject=sub, from_email=settings.EMAIL_HOST_EMAIL,
                                 to=[to], body=message)
    msg.content_subtype = "html"
    msg.send()
    print("Mail Sent Successfuly")
