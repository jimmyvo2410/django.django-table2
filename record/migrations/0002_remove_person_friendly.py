# Generated by Django 2.2.5 on 2019-10-01 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='friendly',
        ),
    ]
