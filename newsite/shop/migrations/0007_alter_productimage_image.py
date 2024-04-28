# Generated by Django 5.0.2 on 2024-04-20 19:07

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.upload_product_image, validators=[shop.models.validator_image]),
        ),
    ]