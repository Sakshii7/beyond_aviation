# Generated by Django 4.1.3 on 2022-11-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_alter_section_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
