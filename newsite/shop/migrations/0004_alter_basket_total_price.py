# Generated by Django 5.0.2 on 2024-04-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_basket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]