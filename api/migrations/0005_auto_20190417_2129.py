# Generated by Django 2.2 on 2019-04-17 21:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190411_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='approved_at',
            field=models.DateTimeField(null=True, default=None, verbose_name='date approved'),
        ),
        migrations.AlterField(
            model_name='invite',
            name='requested_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date requested'),
        ),
    ]
