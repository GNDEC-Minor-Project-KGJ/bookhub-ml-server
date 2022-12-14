# Generated by Django 4.1.3 on 2022-12-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('rating', models.FloatField()),
                ('title', models.CharField(max_length=300)),
                ('word_count', models.IntegerField()),
                ('cleaned_desc', models.TextField()),
            ],
        ),
    ]
