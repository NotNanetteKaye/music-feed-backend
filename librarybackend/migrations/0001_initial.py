# Generated by Django 4.1.2 on 2022-10-13 23:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('release_date', models.DateField(default=django.utils.timezone.now, verbose_name='Release Date')),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]