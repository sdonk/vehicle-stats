# Generated by Django 2.0.8 on 2018-09-19 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fuel',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Fuel'},
        ),
        migrations.AlterModelOptions(
            name='mileage',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Mileage'},
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='year_purchased',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='purchased_on',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]