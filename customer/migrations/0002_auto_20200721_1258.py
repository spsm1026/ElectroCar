# Generated by Django 3.0.3 on 2020-07-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.EmailField(max_length=200),
        ),
    ]
