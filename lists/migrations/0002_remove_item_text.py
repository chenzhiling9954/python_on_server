# Generated by Django 3.2.3 on 2022-05-17 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]
