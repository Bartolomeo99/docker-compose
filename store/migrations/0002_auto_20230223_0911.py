# Generated by Django 3.1.7 on 2023-02-23 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]