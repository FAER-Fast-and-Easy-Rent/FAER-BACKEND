# Generated by Django 4.0.1 on 2022-01-14 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('home_type', models.CharField(choices=[('R', 'ROOM'), ('F', 'FLAT'), ('A', 'APPARTMENT'), ('H', 'HOUSE')], max_length=1)),
                ('room_type', models.CharField(choices=[('S', 'Single'), ('D', 'Double'), ('T', 'Triple'), ('Q', 'Queen'), ('K', 'King')], max_length=1)),
                ('total_occupancy', models.IntegerField(blank=True, null=True)),
                ('total_bedrooms', models.IntegerField(blank=True, null=True)),
                ('total_bathrooms', models.IntegerField(blank=True, null=True)),
                ('is_furnished', models.BooleanField(blank=True, null=True)),
                ('has_kitchen', models.BooleanField(blank=True, null=True)),
                ('has_internet', models.BooleanField(blank=True, null=True)),
                ('has_parking', models.BooleanField(blank=True, null=True)),
                ('has_garden', models.BooleanField(blank=True, null=True)),
                ('has_terrace', models.BooleanField(blank=True, null=True)),
                ('min_stay', models.IntegerField(blank=True, null=True)),
                ('max_stay', models.IntegerField(blank=True, null=True)),
                ('floor_no', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('mime_type', models.CharField(blank=True, max_length=50, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='contenttypes.contenttype')),
            ],
        ),
    ]
