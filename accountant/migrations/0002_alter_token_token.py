# Generated by Django 4.2.7 on 2023-12-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default='xk0FtaFSCyoZWvDL4CHuKjpEgLKlj0', max_length=30),
        ),
    ]
