# Generated by Django 4.1.3 on 2022-12-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0059_serviceoffering_show_on_about_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_type',
            field=models.CharField(choices=[('other', 'Other'), ('owner', 'Owner')], default='other', max_length=20),
        ),
    ]