# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'CATEGORIES'

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    in_stock = models.CharField(max_length=3)
    name = models.CharField(max_length=45)
    image = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    weight = models.IntegerField()
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=45)
    status = models.CharField(max_length=20, blank=True, null=True)
    customer = models.ForeignKey('Customers', models.CASCADE, db_column='customer', blank=True, null=True, default=None)
    category = models.ForeignKey(Categories, models.CASCADE, db_column='category')
    warehouse = models.ForeignKey('Warehouses', models.CASCADE, db_column='warehouse')

    def toString(self):
        ret_str = "name: %s\nprice: %s\ncolor: %s\ndescription: %s\nweight: %d\nquantity: %d" % (self.name, self.price, self.color, self.description, self.weight, self.quantity)
        return ret_str

    class Meta:
        managed = True
        db_table = 'PRODUCTS'


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    region = models.ForeignKey('Regions', models.CASCADE, db_column='region', blank=True, null=True)
    user = models.ForeignKey('Users', models.CASCADE, db_column='user', blank=True, null=True)
    cust_prods = models.ManyToManyField(Products)
    products = []


    class Meta:
        managed = True
        db_table = 'CUSTOMERS'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'USERS'


class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    job_role = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=12)
    sex = models.CharField(max_length=10)
    region = models.ForeignKey('Regions', models.CASCADE, db_column='region')
    warehouse = models.ForeignKey('Warehouses', models.CASCADE, db_column='warehouse')
    user = models.ForeignKey('Users', models.CASCADE, db_column='user', blank=True, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'EMPLOYEES'


class Regions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'REGIONS'


class Warehouses(models.Model):
    id = models.IntegerField(primary_key=True)
    region = models.ForeignKey(Regions, models.CASCADE, db_column='region')
    name = models.CharField(max_length=20)
    size = models.IntegerField()
    address = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    #manager = models.ForeignKey(Employees, models.CASCADE, db_column='manager', blank=True, null=True, default=None)
    manager = models.OneToOneField(Employees, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'warehouses'
