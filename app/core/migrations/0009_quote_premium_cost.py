# Generated by Django 3.1.6 on 2021-02-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210201_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='premium_cost',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=4),
        ),
    ]
