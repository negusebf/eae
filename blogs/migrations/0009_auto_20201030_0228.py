# Generated by Django 2.2.3 on 2020-10-30 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20201029_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_cover_image',
            field=models.ImageField(blank=True, upload_to='img/blogs'),
        ),
    ]
