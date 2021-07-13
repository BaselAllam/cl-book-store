# Generated by Django 3.1.7 on 2021-03-20 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('writer', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(default='', max_length=50)),
                ('book_cover', models.ImageField(upload_to='books')),
                ('book_description', models.CharField(default='', max_length=225)),
                ('audio', models.FileField(upload_to='books/audio')),
                ('pdf', models.FileField(upload_to='books/pdf')),
                ('is_popular', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='categories.categories')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='writer.writer')),
            ],
        ),
    ]