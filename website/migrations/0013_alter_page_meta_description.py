# Generated by Django 4.1.5 on 2023-01-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0012_alter_page_meta_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="meta_description",
            field=models.CharField(max_length=400, null=True),
        ),
    ]
