# Generated by Django 4.1.4 on 2022-12-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_setting_common_service_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='queryform',
            name='email_as_send',
            field=models.BooleanField(default=False),
        ),
    ]
