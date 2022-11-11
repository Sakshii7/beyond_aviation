# Generated by Django 4.1.3 on 2022-11-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_service_excerpt_alter_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOffering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(null=True, upload_to='icons')),
            ],
        ),
    ]
