# Generated by Django 2.0.2 on 2018-03-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calen', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='movies',
            new_name='cartoon',
        ),
        migrations.RenameModel(
            old_name='cartoons',
            new_name='movie',
        ),
    ]
