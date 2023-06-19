# Generated by Django 4.1.5 on 2023-05-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_rename_newletters_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('besoin', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
