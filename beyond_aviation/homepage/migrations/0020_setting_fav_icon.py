# Generated by Django 4.1.4 on 2022-12-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_section_show_mail_us_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='fav_icon',
            field=models.ImageField(blank=True, null=True, upload_to='FavIcon'),
        ),
    ]
