# Generated by Django 4.1.3 on 2022-12-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0043_alter_service_excerpt_alter_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='service',
        ),
        migrations.AddField(
            model_name='menu',
            name='show_in_footer',
            field=models.BooleanField(default=False),
        ),
    ]