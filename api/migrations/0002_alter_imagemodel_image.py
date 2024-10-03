# Generated by Django 4.2.5 on 2024-09-27 01:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='images/', validators=[api.models.validate_image_or_svg]),
        ),
    ]
