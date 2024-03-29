# Generated by Django 5.0.1 on 2024-01-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0002_alter_product_cat"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="pimage",
            field=models.ImageField(default=0, upload_to="image"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="cat",
            field=models.IntegerField(
                choices=[(1, "Choclate"), (2, "Farsans"), (3, "Rice")],
                max_length=50,
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Product Name"),
        ),
        migrations.AlterField(
            model_name="product",
            name="pdetail",
            field=models.CharField(max_length=400, verbose_name="Product Detail"),
        ),
    ]
