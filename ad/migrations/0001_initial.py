# Generated by Django 2.2.10 on 2020-05-22 02:41

import ad.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('postDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('featured', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=3)),
                ('views', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=100)),
                ('expiryDate', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Detail',
                'verbose_name_plural': 'Details',
            },
        ),
        migrations.CreateModel(
            name='Dish_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Dish Menu',
                'verbose_name_plural': 'Dish Menus',
            },
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='model/def.jfif', null=True, upload_to=ad.models.upload_location)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitting_capacity', models.IntegerField()),
                ('category', models.CharField(choices=[('Banquet Hall', 'Banquet Hall'), ('Marquee', 'Marquee'), ('Hotel Hall', 'Hotel Hall'), ('Farmhouse', 'Farmhouse'), ('Lawn', 'Lawn')], default='Banquet Hall', max_length=50)),
                ('parking_capacity', models.IntegerField()),
                ('air_conditioner', models.BooleanField(blank=True, default=False, null=True)),
                ('heater', models.BooleanField(blank=True, default=False, null=True)),
                ('dj_system', models.BooleanField(blank=True, default=False, null=True)),
                ('wifi', models.BooleanField(blank=True, default=False, null=True)),
                ('bridal_room', models.BooleanField(blank=True, default=False, null=True)),
                ('valet_parking', models.BooleanField(blank=True, default=False, null=True)),
                ('decoration', models.BooleanField(blank=True, default=False, null=True)),
                ('generator', models.BooleanField(blank=True, default=False, null=True)),
                ('outside_catering', models.BooleanField(blank=True, default=False, null=True)),
                ('outside_dj', models.BooleanField(blank=True, default=False, null=True)),
                ('outside_decoration', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'verbose_name': 'Venue',
                'verbose_name_plural': 'Venues',
            },
        ),
        migrations.CreateModel(
            name='VenuePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_guest', models.IntegerField()),
                ('heater', models.IntegerField()),
                ('dj_system', models.IntegerField()),
                ('decoration', models.IntegerField()),
                ('wiFi', models.IntegerField()),
                ('BridalRoom', models.IntegerField(default=0)),
                ('venue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad.Venue', verbose_name='Venue')),
            ],
            options={
                'verbose_name': 'Venue Price',
                'verbose_name_plural': 'Venue Prices',
            },
        ),
    ]
