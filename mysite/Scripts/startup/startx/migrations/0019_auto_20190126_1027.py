# Generated by Django 2.1.4 on 2019-01-26 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startx', '0018_auto_20190125_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='startx.Profile'),
        ),
    ]
