# Generated by Django 2.1.5 on 2019-02-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_auto_20190130_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='recursos'),
        ),
    ]
