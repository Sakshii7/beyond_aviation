# Generated by Django 4.1.3 on 2022-11-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_alter_service_excerpt_alter_service_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
