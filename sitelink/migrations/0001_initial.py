# Generated by Django 3.1.5 on 2021-03-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebookLink', models.CharField(max_length=225)),
                ('siteLink', models.CharField(max_length=225)),
            ],
        ),
    ]