# Generated by Django 3.2.3 on 2021-06-10 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myJourneys', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myJourneys.vehicle'),
        ),
    ]
