# Generated by Django 3.2.3 on 2021-06-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myJourneys', '0002_auto_20210610_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_user', max_length=30),
        ),
    ]
