# Generated by Django 4.1.4 on 2023-01-03 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_slider_alter_section_text_align_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slides',
            old_name='section',
            new_name='slide',
        ),
    ]
