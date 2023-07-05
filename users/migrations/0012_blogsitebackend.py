# Generated by Django 4.1.9 on 2023-07-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_requestquote_delete_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogSiteBackend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogImage', models.ImageField(null=True, upload_to='static/blog/Blog Image')),
                ('blogRelatedTitle', models.CharField(max_length=50)),
                ('writterName', models.CharField(max_length=50)),
                ('publishDate', models.DateField()),
                ('blogTitle', models.CharField(max_length=200)),
                ('blogDetail', models.TextField()),
            ],
        ),
    ]