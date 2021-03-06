# Generated by Django 3.1.5 on 2021-01-31 23:22

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_paymentlistmonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policy_id', models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('expire', models.DateField(blank=True, db_index=True, default=core.models.next_year, null=True, verbose_name='expire')),
                ('active', models.BooleanField(db_index=True, default=True, verbose_name='active')),
                ('policy_paymentListMonth_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.paymentlistmonth', verbose_name='payment list Month')),
                ('policy_quote_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.quote', verbose_name='quote')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
