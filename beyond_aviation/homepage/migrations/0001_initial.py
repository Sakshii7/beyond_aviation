# Generated by Django 4.1.4 on 2022-12-15 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('show_in_footer', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Homepage Logo')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
            ],
            options={
                'db_table': 'menu',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('header_img', models.ImageField(blank=True, null=True, upload_to='Header Image')),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pages',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='QueryForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'query_form',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('text_align', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='left', max_length=10)),
                ('section_type', models.CharField(choices=[('other', 'Other'), ('owner', 'Owner')], default='other', max_length=20)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
                ('image', models.ImageField(null=True, upload_to='Section')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'section',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('excerpt', models.CharField(blank=True, max_length=450, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Service')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_flag', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'services',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='ServiceOffering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='ServiceOffering')),
                ('text_align', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], default='left', max_length=10)),
                ('show_on_about_page', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'service_offering',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_address', models.TextField()),
                ('facebook_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('twitter_url', models.URLField()),
            ],
            options={
                'db_table': 'setting',
            },
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('section_icon', models.ImageField(blank=True, null=True, upload_to='SubSection')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'InActive')], default='inactive', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.section')),
            ],
            options={
                'db_table': 'sub_section',
                'ordering': ['created_on'],
            },
        ),
    ]
