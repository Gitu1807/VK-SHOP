# Generated by Django 5.0.1 on 2024-01-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0010_about_contact_facebook_home"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instagram",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("pimage", models.ImageField(upload_to="image")),
            ],
        ),
        migrations.CreateModel(
            name="Twitter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("pimage", models.ImageField(upload_to="image")),
            ],
        ),
    ]
