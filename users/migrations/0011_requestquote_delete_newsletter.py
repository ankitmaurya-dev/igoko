# Generated by Django 4.1.9 on 2023-07-05 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_lovefromclient_clientimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('SelectedService', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='newsletter',
        ),
    ]
