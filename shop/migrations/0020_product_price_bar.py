# Generated by Django 4.1.5 on 2023-06-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_product_pop'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_bar',
            field=models.FloatField(default=200),
            preserve_default=False,
        ),
    ]
