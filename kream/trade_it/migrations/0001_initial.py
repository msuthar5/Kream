# Generated by Django 2.0 on 2018-04-17 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'CATEGORIES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'CUSTOMERS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=100)),
                ('job_role', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=12)),
                ('sex', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'EMPLOYEES',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('in_stock', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=45)),
                ('image', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=45)),
                ('weight', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=45)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('category', models.ForeignKey(db_column='category', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Categories')),
            ],
            options={
                'db_table': 'PRODUCTS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'REGIONS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'USERS',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('manager', models.ForeignKey(db_column='manager', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Employees')),
                ('region', models.ForeignKey(db_column='region', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Regions')),
            ],
            options={
                'db_table': 'warehouses',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Users'),
        ),
        migrations.AddField(
            model_name='products',
            name='warehouse',
            field=models.ForeignKey(db_column='warehouse', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Warehouses'),
        ),
        migrations.AddField(
            model_name='employees',
            name='region',
            field=models.ForeignKey(db_column='region', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Regions'),
        ),
        migrations.AddField(
            model_name='employees',
            name='warehouse',
            field=models.ForeignKey(db_column='warehouse', on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Warehouses'),
        ),
        migrations.AddField(
            model_name='customers',
            name='cust_products',
            field=models.ManyToManyField(to='trade_it.Products'),
        ),
        migrations.AddField(
            model_name='customers',
            name='region',
            field=models.ForeignKey(blank=True, db_column='region', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Regions'),
        ),
        migrations.AddField(
            model_name='customers',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trade_it.Users'),
        ),
    ]
