# Generated by Django 3.1.4 on 2020-12-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstpage', '0010_plants_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='image',
            field=models.ImageField(default='rose.jpg', upload_to='images/plants/'),
        ),
    ]