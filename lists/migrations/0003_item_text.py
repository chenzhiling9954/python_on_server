# Generated by Django 3.2.3 on 2022-05-17 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_remove_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
