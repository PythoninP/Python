# Generated by Django 4.1.6 on 2023-03-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppToddo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2020-5-7'),
            preserve_default=False,
        ),
    ]
