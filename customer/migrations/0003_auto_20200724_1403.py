# Generated by Django 3.0.3 on 2020-07-24 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_bookmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='bookmark_address',
            new_name='bookmark_station',
        ),
    ]