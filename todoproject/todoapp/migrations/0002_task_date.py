# Generated by Django 4.2.7 on 2023-11-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-04'),
            preserve_default=False,
        ),
    ]
