# Generated by Django 2.2.3 on 2020-10-30 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20201025_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trending',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
