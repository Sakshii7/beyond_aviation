# Generated by Django 4.1.3 on 2022-12-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0046_remove_contact_contact_contact_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'main_app_user',
                'managed': False,
                'default_permissions': 'view',
            },
        ),
    ]