# Generated by Django 2.2 on 2019-04-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190417_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='approved_at',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='date approved'),
        ),
    ]