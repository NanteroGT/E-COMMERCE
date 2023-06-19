# Generated by Django 4.1.5 on 2023-05-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_commande_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newletters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_email', models.EmailField(max_length=254)),
                ('date_email', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_email'],
            },
        ),
    ]
