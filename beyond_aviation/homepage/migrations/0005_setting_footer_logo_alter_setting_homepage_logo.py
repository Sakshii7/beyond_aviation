# Generated by Django 4.1.4 on 2022-12-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_rename_image_service_service_image_remove_menu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='footer_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Footer Logo'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='homepage_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Homepage Logo'),
        ),
    ]
