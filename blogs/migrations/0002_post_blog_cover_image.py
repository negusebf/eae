# Generated by Django 2.2.3 on 2020-10-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_cover_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
