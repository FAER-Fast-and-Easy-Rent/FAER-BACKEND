# Generated by Django 4.0.3 on 2022-03-11 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('capacity', models.IntegerField()),
                ('vehicle_type', models.CharField(max_length=100)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('plate_number', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('home_type', models.CharField(max_length=100)),
                ('room_type', models.CharField(max_length=100)),
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
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=255)),
                ('mime_type', models.CharField(blank=True, max_length=100, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
