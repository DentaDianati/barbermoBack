# Generated by Django 5.1.1 on 2024-10-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.IntegerField(unique=True),
        ),
    ]
