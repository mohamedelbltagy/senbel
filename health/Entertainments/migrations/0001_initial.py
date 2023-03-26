# Generated by Django 4.1.3 on 2023-03-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entertainments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('telephone_number', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200)),
                ('locations', models.CharField(max_length=200)),
                ('features', models.TextField(max_length=500, null=True)),
                ('opening_hours', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]