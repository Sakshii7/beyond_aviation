# Generated by Django 4.1.3 on 2022-11-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0022_subsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='text_align',
            field=models.IntegerField(choices=[(0, ''), (1, 'Left'), (2, 'Right')], default=0),
        ),
        migrations.AddField(
            model_name='subsection',
            name='section_icon',
            field=models.ImageField(null=True, upload_to='section_icons'),
        ),
    ]