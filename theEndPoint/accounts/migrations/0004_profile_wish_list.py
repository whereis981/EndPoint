# Generated by Django 5.1.2 on 2024-11-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_user'),
        ('peaks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wish_list',
            field=models.ManyToManyField(blank=True, related_name='wished_by', to='peaks.peak'),
        ),
    ]
