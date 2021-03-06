# Generated by Django 4.0.4 on 2022-05-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('total', models.PositiveBigIntegerField(blank=True)),
                ('total_price', models.PositiveBigIntegerField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('cars', models.ManyToManyField(to='cars.car')),
            ],
        ),
    ]
