# Generated by Django 2.0 on 2018-04-21 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade_it', '0012_auto_20180421_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouses',
            name='manager',
            field=models.ForeignKey(blank=True, db_column='manager', null=True, on_delete=django.db.models.deletion.CASCADE, to='trade_it.Employees'),
        ),
    ]
