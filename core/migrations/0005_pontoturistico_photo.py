# Generated by Django 2.1.5 on 2019-02-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190131_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
