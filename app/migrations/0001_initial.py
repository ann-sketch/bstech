# Generated by Django 3.1.5 on 2021-01-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('email', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('number', models.CharField(blank=True, max_length=15)),
                ('password', models.CharField(max_length=256)),
                ('product_key', models.CharField(default='', max_length=256)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
