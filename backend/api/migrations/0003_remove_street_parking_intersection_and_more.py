# Generated by Django 5.0.4 on 2024-05-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_parking_place_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='street_parking',
            name='intersection',
        ),
        migrations.AddField(
            model_name='street_parking',
            name='street1',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='street_parking',
            name='street2',
            field=models.CharField(default='', max_length=255),
        ),
    ]