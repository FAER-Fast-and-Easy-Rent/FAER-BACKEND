# Generated by Django 3.2.3 on 2021-05-24 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210524_1215'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amenities',
            new_name='Amenitie',
        ),
        migrations.RenameModel(
            old_name='HouseRules',
            new_name='HouseRule',
        ),
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
