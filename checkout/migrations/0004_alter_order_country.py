# Generated by Django 5.0.2 on 2024-07-02 15:33

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0003_alter_order_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="country",
            field=models.CharField(max_length=40),
        ),
    ]
