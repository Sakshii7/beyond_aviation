# Generated by Django 4.1.3 on 2022-12-21 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0014_rename_section_icon_subsection_icon_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="serviceoffering",
            old_name="image",
            new_name="icon",
        ),
    ]