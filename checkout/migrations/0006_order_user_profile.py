# Generated by Django 5.0.2 on 2024-07-03 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0005_alter_order_country"),
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="user_profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="orders",
                to="profiles.userprofile",
            ),
        ),
    ]
