# Generated by Django 4.1.5 on 2023-05-02 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_pricex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pricex',
        ),
    ]
