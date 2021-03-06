# Generated by Django 2.1.5 on 2019-01-30 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
        ('comments', '0001_initial'),
        ('recursos', '0003_auto_20190130_1610'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.Address')),
                ('comments', models.ManyToManyField(to='comments.Comment')),
                ('resources', models.ManyToManyField(to='recursos.Recurso')),
                ('reviews', models.ManyToManyField(to='reviews.Review')),
            ],
        ),
    ]
