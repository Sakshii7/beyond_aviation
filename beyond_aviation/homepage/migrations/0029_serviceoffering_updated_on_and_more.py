# Generated by Django 4.1.3 on 2022-11-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0028_alter_subsection_section_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceoffering",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="serviceoffering",
            name="created_on",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]