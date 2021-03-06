# Generated by Django 2.2.3 on 2020-10-27 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='image',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='text',
        ),
        migrations.AddField(
            model_name='articles',
            name='author_photo',
            field=models.ImageField(blank=True, upload_to='img/article/author'),
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
