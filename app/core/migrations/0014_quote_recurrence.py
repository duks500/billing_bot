# Generated by Django 3.1.6 on 2021-02-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210209_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='recurrence',
            field=models.CharField(blank=True, choices=[('Monthly', 'Monthly'), ('Yearly', 'Yearly')], default='Yearly', max_length=255),
        ),
    ]