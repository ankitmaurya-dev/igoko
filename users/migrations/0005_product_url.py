# Generated by Django 4.2.2 on 2023-06-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
