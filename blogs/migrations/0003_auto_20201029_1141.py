# Generated by Django 2.2.3 on 2020-10-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_blog_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
