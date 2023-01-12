# Generated by Django 4.1.5 on 2023-01-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "website",
            "0010_rename_google_tag_manager_body_key_setting_google_tag_manager_key_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="meta_description",
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="meta_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="MetaImage", verbose_name="Meta Image"
            ),
        ),
        migrations.AddField(
            model_name="page",
            name="meta_keywords",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="page",
            name="meta_title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
