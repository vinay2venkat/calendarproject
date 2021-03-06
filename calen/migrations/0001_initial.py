# Generated by Django 2.0.2 on 2018-03-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartoons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=100)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('size', models.CharField(max_length=100)),
            ],
        ),
    ]
