# Generated by Django 5.0.1 on 2024-01-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0008_order_orderid"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amt",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
