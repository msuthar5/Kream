from django.shortcuts import render, get_object_or_404
from trade_it import forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def confirm_login(username, password):
    users = Users.objects.all()

    for u in users:
        if u.username == username and u.password == password:
            return True

    return False


def managers_products(request,manager_id):

    manager = get_object_or_404(Employees, pk=manager_id)
    products = []

    for p in Products.objects.all():
        if p.warehouse == manager.warehouse:
            products.append(p)

    return render(request, 'trade_it/manager_products.html', {'products': products, 'manager': manager})


def update_info_controller(request, customer_id):

    customer = get_object_or_404(Customers, pk=customer_id)
    user = customer.user

    if request.method == 'POST':
        form = forms.UpdateInfoForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            address = form.cleaned_data['address']

            if username != '':
                user.username = username
                user.save()
            if password != '':
                user.password = password
                user.save()

            if first_name != '':
                customer.first_name = first_name
            else:
                print('Got None')
            if last_name != '':
                customer.last_name = last_name
            if email_address != '':
                customer.email_address = email_address
            if address != '':
                customer.address = address

            customer.save()

            return render(request, 'trade_it/update_info.html', {'form': form, 'customer': customer, 'user': user})
        return render(request, 'trade_it/update_info.html', {'form': form, 'customer': customer, 'user': user})

    else:
        form = forms.UpdateInfoForm()
        return render(request, 'trade_it/update_info.html', {'form': form, 'customer': customer, 'user': user})


def purchase_product_controller(request,product_id, **kwargs):
    product = get_object_or_404(Products, pk=product_id)
    products = Products.objects.all()

    if request.method == 'POST':

        form = forms.PurchaseProductForm(request.POST)
        if form.is_valid():

            product.quantity -= 1

            if product.quantity == 0:

                product.in_stock = 'No'

            product.save()

            query_form = forms.QueryProductsForm()
            return render(request, 'trade_it/query_view.html', {'form': query_form, 'products': products})
        return render(request, 'trade_it/purchase_product.html', {'form': form, 'product': product})

    else:

        form = forms.PurchaseProductForm()
        return render(request,'trade_it/purchase_product.html', {'form': form, 'product': product})


def admin_view(request, admin_id):

    admin = get_object_or_404(Users, pk=admin_id)
    customers = list(Customers.objects.all())
    managers = []
    employees = []

    for e in Employees.objects.all():
        if e.job_role != 'manager':
            employees.append(e)
        else:
            managers.append(e)

    users = Users.objects.all()
    regions = Regions.objects.all()
    warehouses = Warehouses.objects.all()
    products = Products.objects.all()
    categories = Categories.objects.all

    return render(request, 'trade_it/admin_view.html', {
                                                        'admin': admin,
                                                        'users': users,
                                                        'regions': regions,
                                                        'warehouses': warehouses,
                                                        'products': products,
                                                        'categories': categories,
                                                        'customers': customers,
                                                        'managers' : managers,
                                                        'employees': employees
                                                        })


def admin_customers(request, admin_id):

    customers = list(Customers.objects.all())

    return render(request, 'trade_it/admin_customers.html', {'customers': customers})


def admin_managers(request, admin_id):

    managers = []
    employees = []

    for e in Employees.objects.all():
        if e.job_role != 'manager':
            employees.append(e)
        else:
            managers.append(e)

    return render(request, 'trade_it/admin_managers.html', {'managers': managers})


def admin_employees(request, admin_id):

    managers = []
    employees = []

    for e in Employees.objects.all():
        if e.job_role != 'manager':
            employees.append(e)
        else:
            managers.append(e)

    return render(request, 'trade_it/admin_employees.html', {'employees': employees})


def bounds(str):
    b1 = b2 = ''
    i = 1

    while str[i] is not '-':
        b1 += str[i]
        i += 1
    b2 = str[i+2:]
    return float(b1), float(b2)


def cust_view(request, customer_id):

    customer = get_object_or_404(Customers, pk = customer_id)
    prod = Products.objects.all()
    products = []

    for p in prod:
        if p.customer == customer:
            products.append(p)

    return render(request, 'trade_it/user_view.html', {'customer': customer, 'products': products})


def add_employee(request, manager_id):
    manager = get_object_or_404(Employees, pk=manager_id)

    if request.method == 'POST':
        form = forms.AddEmployeeForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            sex = form.cleaned_data['sex']
            job_role = form.cleaned_data['job_role']
            address = form.cleaned_data['address']

            u = Users()
            u.id = len(Users.objects.all()) + 1
            u.username = username
            u.password = password
            u.role = 'employee'
            u.save()

            e = Employees()
            e.id = len(Employees.objects.all()) + 1
            e.first_name = first_name
            e.last_name = last_name
            e.email = email_address
            e.phone_number = phone_number
            e.sex = sex
            e.job_role = job_role
            e.address = address
            e.region = manager.region
            e.warehouse = manager.warehouse
            e.user = u
            e.save()

            return HttpResponseRedirect('../../../' + str(manager_id) + '/manager-view')
            #return render(request, 'trade_it/' + str(manager.id) + '/manager-view'+'/manager_view.html', {'manager': manager, 'employees': employees})
        return render(request, 'trade_it/add_employee.html', {'manager': manager, 'form': form})

    else:
        form = forms.AddEmployeeForm()
        return render(request, 'trade_it/add_employee.html', {'manager': manager, 'form': form})


def manager_view(request, manager_id):

    manager = get_object_or_404(Employees, pk=manager_id)
    employees = []

    for e in Employees.objects.all():
        if e.warehouse == manager.warehouse and e != manager:
            employees.append(e)

    return render(request, 'trade_it/manager_view.html', {'manager': manager, 'employees': employees})


def employee_view(request, employee_id):

    employee = get_object_or_404(Employees, pk=employee_id)

    return render(request, 'trade_it/employee_view.html', {'employee': employee})


def add_product_view(request, customer_id):

    categories = Categories.objects.all()

    if request.method == 'POST':
        form = forms.AddProductForm(request.POST)

        if form.is_valid():

            cat = form.cleaned_data['category']
            new_cat = form.cleaned_data['new_category']
            name = form.cleaned_data['name']
            color = form.cleaned_data['color']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            weight = form.cleaned_data['weight']
            c = None

            if cat[0] != 'New Category':
                if new_cat != '':
                    raise ValidationError(_('If you want to create a new Category, please select the: Create New Option'))

                else:
                    c = get_object_or_404(Categories, pk=cat[0])

            if c is None:
                c = Categories(id=len(Categories.objects.all()) + 1, name=new_cat)
                c.save()

            cust = get_object_or_404(Customers, pk=customer_id)
            r = cust.region

            w = Warehouses.objects.all().filter(region=r)[0]

            p = Products()
            p.id = len(Products.objects.all()) + 1
            p.name = name
            p.color = color
            p.description = description
            p.price = price
            p.quantity = quantity
            p.weight = int(weight)
            p.status = "in stock"
            p.category = c
            p.in_stock = "Yes"
            p.customer = cust
            p.warehouse = w
            p.save()

            return HttpResponseRedirect('../../../'+str(cust.id) + '/customer-view')
        return render(request, 'trade_it/add_product.html', {'form': form})

    else:
        form = forms.AddProductForm()
        return render(request, 'trade_it/add_product.html', {'form': form})


def get_role(user):

    if user.role == "customer":
        return "user_view.html"
    if user.role == "employee":
        return "employee_view.html"
    if user.role == "manager":
        return "manager_view.html"


def index(request):

    return HttpResponse("Welcome to the customer portal")


def login_controller(request):

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():

            customers = Customers.objects.all()
            employees = Employees.objects.all()
            customer = None
            manager = None
            employee = None
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            user = Users.objects.filter(username=uname)[0]

            if confirm_login(uname, pword):

                if user.role == "admin":

                    return HttpResponseRedirect(str(user.id) + '/admin-view')
                if user.role == "customer":

                    for c in customers:
                        if c.user == user:
                            customer = c

                    return HttpResponseRedirect(str(customer.id) + '/customer-view')
                elif user.role == "manager":

                    for e in employees:
                        if e.user == user:
                            manager = e

                    return HttpResponseRedirect(str(manager.id) + '/manager-view')

                for e in employees:
                    if e.user == user:
                        employee = e

                return HttpResponseRedirect(str(employee.id) + '/employee-view')

            # login failed
            return render(request, 'trade_it/login.html', {'form': form} )

        return render(request, 'trade_it/login.html', {'form': form})
    else:

        form = forms.LoginForm()
        return render(request, 'trade_it/login.html', {'form': form} )


def customer_info_controller(request, u):

    if request.method == 'POST':
        form = forms.CustomerInfoForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            address = form.cleaned_data['address']
            u = None

            c = Customers()
            c.id = len(Customers.objects.all()) + 1
            c.first_name = first_name
            c.last_name = last_name
            c.email_address = email_address
            c.address = address

            uname = (first_name[0] + last_name).lower()

            users = Users.objects.all()

            for a in users:
                if a.username == uname:
                    u = a

            c.user = u
            c.save()

            f = forms.LoginForm()
            return render(request, 'trade_it/')
        return render(request, 'trade_it/customer_info.html', {'form': form})

    else:
        form = forms.CustomerInfoForm()
        return render(request, 'trade_it/customer_info.html', {'form': form, 'user': u})


def registration_controller(request):

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            address = form.cleaned_data['address']
            region = form.cleaned_data['region']

            l = len(Users.objects.all())

            # create user
            u = Users()
            u.id = l + 1
            u.username = uname
            u.password = pword
            u.role = "customer"
            u.save()

            c = Customers()
            c.id = len(Customers.objects.all()) + 1
            c.first_name = first_name
            c.last_name = last_name
            c.email_address = email_address
            c.address = address
            c.user = u
            c.region = get_object_or_404(Regions, pk=region[0])
            c.save()

            return HttpResponseRedirect('../' + str(c.id) + '/customer-view')

        return render(request, 'trade_it/register.html', {'form': form})
    else:

        form = forms.RegisterForm()
        return render(request, 'trade_it/register.html', {'form': form})


def productQueryController(request, customer_id):
    products_query = Products.objects.all()
    keywords_query = Products.objects.all()
    products = []
    prods = []
    return_prods = []
    kw_list = []
    ret_set = set()
    price_set = None
    cat_set = None
    keyword_set = None

    for p in products_query:
        products.append(p)

    key_prods = []
    low = -10000000.0
    high = 10000000.0

    if request.method == 'POST':
        form = forms.QueryProductsForm(request.POST)
        if form.is_valid():

            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            keyword = form.cleaned_data['keyword']

            if len(category) != 0:
                products_query = Products.objects.raw('SELECT * FROM Products WHERE Products.category=%d' % int(category[0]))
                for p in products_query:
                    return_prods.append(p)
                    cat_set = set(return_prods)

            else:
                cat_set = set(products)
                return_prods = products

            if len(price) != 0:
                price = price[0]
                low, high = bounds(price)
                for p in products:
                    if low <= float(p.price) <= high:
                        print(p.price)
                        prods.append(p)
                        price_set = set(prods)
                    else:
                        pass

            if keyword is not None:

                for p in keywords_query:
                    if keyword in p.name or keyword in p.description:
                        kw_list.append(p)

                keyword_set = set(kw_list)
            if price_set and keyword_set and cat_set:
                ret_set = keyword_set.intersection(cat_set).intersection(price_set)
            elif price_set and cat_set and not keyword_set:
                ret_set = cat_set.intersection(price_set)
            elif price_set and keyword_set and not cat_set:
                ret_set = price_set.intersection(cat_set)
            elif price_set and not keyword_set and not cat_set:
                ret_set = price_set
            elif keyword_set and cat_set and not price_set:
                ret_set = keyword_set.intersection(cat_set)
            elif keyword_set and not cat_set and not price_set:
                ret_set = keyword_set
            else:
                ret_set = products

            return_prods = list(ret_set)

            return render(request, 'trade_it/query_view.html', {'form': form, 'products': return_prods})
        else:
            #code
            return render(request, 'trade_it/query_view.html', {'form': form, 'products': products})

    else:
        form = forms.QueryProductsForm()
        form.prods = prods
        return render(request, 'trade_it/query_view.html', {'form': form, 'products': products})
