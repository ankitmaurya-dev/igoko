# Generated by Django 4.2.2 on 2023-06-12 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_product_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='service',
        ),
    ]
