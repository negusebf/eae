# Generated by Django 2.2.3 on 2020-10-30 02:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20201030_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_cover_image',
            field=models.ImageField(default=datetime.datetime(2020, 10, 30, 2, 37, 8, 155926, tzinfo=utc), upload_to='img/blogs'),
        ),
    ]
