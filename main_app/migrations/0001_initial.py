# Generated by Django 3.1.3 on 2020-11-12 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=100)),
            ],
        ),
    ]
