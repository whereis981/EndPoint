# Generated by Django 5.1.2 on 2024-11-20 18:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'A peak with that name already exists!'}, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('elevation', models.DecimalField(decimal_places=3, max_digits=4)),
                ('mountain_range', models.CharField(choices=[('Himalayas', 'Himalayas'), ('Karakoram', 'Karakoram')], max_length=50)),
                ('first_ascent_date', models.DateField(help_text='Enter the date of the first ascent (YYYY-MM-DD)')),
                ('first_climbers', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='peaks_image/')),
                ('death_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('description', models.TextField()),
            ],
        ),
    ]