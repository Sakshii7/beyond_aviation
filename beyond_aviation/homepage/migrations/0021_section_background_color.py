# Generated by Django 4.1.4 on 2022-12-26 05:05

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_setting_fav_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='background_color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
    ]
