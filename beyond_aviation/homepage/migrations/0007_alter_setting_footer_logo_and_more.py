# Generated by Django 4.1.4 on 2022-12-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_setting_footer_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
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