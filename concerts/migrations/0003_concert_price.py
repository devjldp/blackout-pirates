# Generated by Django 5.0.2 on 2024-06-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerts', '0002_rename_concerts_concert'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]