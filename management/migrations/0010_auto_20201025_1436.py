# Generated by Django 2.2.3 on 2020-10-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_ads_articles_blogs_linkedvideos_localvideos_photos_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeview',
            name='display_row',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
