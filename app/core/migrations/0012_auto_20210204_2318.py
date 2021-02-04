# Generated by Django 3.1.6 on 2021-02-04 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210204_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policy',
            name='quote_number',
        ),
        migrations.AlterField(
            model_name='policy',
            name='paymentListMonth_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.paymentlistmonth', verbose_name='payment list Month'),
        ),
    ]
