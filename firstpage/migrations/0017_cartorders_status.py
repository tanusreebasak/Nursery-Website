# Generated by Django 3.1.4 on 2020-12-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0016_auto_20201231_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]