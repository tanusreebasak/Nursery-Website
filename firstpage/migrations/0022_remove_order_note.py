# Generated by Django 3.1.4 on 2020-12-31 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0021_auto_20201231_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
    ]
