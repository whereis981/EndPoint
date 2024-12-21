# Generated by Django 5.1.2 on 2024-11-29 11:46

import django.core.validators
import theEndPoint.peaks.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peaks', '0002_alter_peak_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peak',
            name='death_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='peak',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='peaks_image/', validators=[theEndPoint.peaks.validators.image_size_validator]),
        ),
    ]
