# Generated by Django 3.2.3 on 2021-05-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_rename_datetradeplace_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='pnl',
            field=models.FloatField(null=True),
        ),
    ]
