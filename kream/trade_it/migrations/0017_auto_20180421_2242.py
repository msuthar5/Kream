# Generated by Django 2.0 on 2018-04-21 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_it', '0016_auto_20180421_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouses',
            name='manager',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trade_it.Employees'),
        ),
    ]
