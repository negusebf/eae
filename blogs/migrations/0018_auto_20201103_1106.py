# Generated by Django 2.2.3 on 2020-11-03 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_post_post_labe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_labe',
            new_name='post_label',
        ),
    ]
