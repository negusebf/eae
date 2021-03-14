# Generated by Django 2.2.3 on 2020-11-18 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0032_emailsender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsender',
            name='e_from',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='emailsender',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='emailsender',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
