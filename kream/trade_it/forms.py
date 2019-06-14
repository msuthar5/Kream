from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from trade_it.models import *


class LoginForm(forms.Form):

    username = forms.CharField(help_text="enter your username. ")
    password = forms.CharField(help_text="enter your password. ")

    def clean_username(self):

        uname = self.cleaned_data['username']

        unames = Users.objects.values_list('username')

        for i in range(len(unames)):
            if uname == unames[i][0]:

                return uname

        raise ValidationError(_('invalid username'))

    def clean_password(self):

        pword = self.cleaned_data['password']

        return pword


class RegisterForm(forms.Form):

    regions = Regions.objects.all()

    regs = []

    for r in regions:
        regs.append(
            (r.id, r.name)
        )

    username = forms.CharField(help_text="enter your username. ")
    password = forms.CharField(help_text="enter your password. ")
    #role = forms.CharField(help_text="enter your role: customer, manager, employee")
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.CharField()
    address = forms.CharField()

    region = forms.MultipleChoiceField(

        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=regs,

    )

    def clean_username(self):

        uname = self.cleaned_data['username']

        unames = Users.objects.values_list('username')

        for i in range(len(unames)):
            if uname == unames[i][0]:
                raise ValidationError(_('username already exists'))

        return uname

    def clean_password(self):

        pword = self.cleaned_data['password']

        return pword

    def clean_first_name(self):

        fn = self.cleaned_data['first_name']

        return fn

    def clean_last_name(self):

        ln = self.cleaned_data['last_name']

        return ln

    def clean_email_address(self):

        email = self.cleaned_data['email_address']

        return email

    def clean_address(self):

        addr = self.cleaned_data['address']

        return addr

    def clean_region(self):

        region = self.cleaned_data['region']

        return region


class UpdateInfoForm(forms.Form):

    regions = Regions.objects.all()

    regs = []

    for r in regions:
        regs.append(
            (r.id, r.name)
        )

    username = forms.CharField(help_text="enter your username. ", required=False)
    password = forms.CharField(help_text="enter your password. ", required=False)
    #role = forms.CharField(help_text="enter your role: customer, manager, employee")
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email_address = forms.CharField(required=False)
    address = forms.CharField(required=False)

    region = forms.MultipleChoiceField(

        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=regs,

    )

    def clean_username(self):

        uname = self.cleaned_data['username']

        unames = Users.objects.values_list('username')

        for i in range(len(unames)):
            if uname == unames[i][0]:
                raise ValidationError(_('username already exists'))

        return uname

    def clean_password(self):

        pword = self.cleaned_data['password']

        return pword

    def clean_first_name(self):

        fn = self.cleaned_data['first_name']

        return fn

    def clean_last_name(self):

        ln = self.cleaned_data['last_name']

        return ln

    def clean_email_address(self):

        email = self.cleaned_data['email_address']

        return email

    def clean_address(self):

        addr = self.cleaned_data['address']

        return addr

    def clean_region(self):

        region = self.cleaned_data['region']

        return region


class CustomerInfoForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.CharField()
    address = forms.CharField()

    def clean_first_name(self):

        fn = self.cleaned_data['first_name']

        return fn

    def clean_last_name(self):

        ln = self.cleaned_data['last_name']

        return ln

    def clean_email_address(self):

        email = self.cleaned_data['email_address']

        return email

    def clean_address(self):

        addr = self.cleaned_data['address']

        return addr


class AddProductForm(forms.Form):

    categories = Categories.objects.all()

    cats = []
    cats.append(
        ('New Category', 'Create New Category')
    )

    for c in categories:
        cats.append(
            (c.id, c.name)
        )

    category = forms.MultipleChoiceField(

        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=cats,

    )

    new_category = forms.CharField(initial=None, required=False)
    name = forms.CharField()
    color = forms.CharField()
    description = forms.CharField()
    price = forms.CharField()
    quantity = forms.IntegerField()
    weight = forms.CharField()

    def clean_category(self):

        category = self.cleaned_data['category']

        if len(category) != 1:
            raise ValidationError(_('Please Select 1 option only'))

        return category

    def clean_new_cat(self):

        new_category = self.cleaned_data['new_category']
        category = self.clean_category()

        if category[0] != 'New Category':

            if new_category != '':
                raise ValidationError(_('If you want to create a new Category, please select the: Create New Category'))

        return new_category

    def clean_name(self):

        name = self.cleaned_data['name']

        if len(name) > 45:
            raise ValidationError(_('Name must be < 45 characters'))

        return name

    def clean_color(self):

        color = self.cleaned_data['color']

        if len(color) > 45:
            raise ValidationError(_('Color must be < 45 characters'))

        return color

    def clean_description(self):

        description = self.cleaned_data['description']

        if len(description) > 50:
            raise ValidationError(_('Descrption must be < 50 characters'))

        return description

    def clean_price(self):

        price = self.cleaned_data['price']

        return price

    def clean_quantity(self):

        quantity = self.cleaned_data['quantity']

        return quantity

    def clean_weight(self):

        weight = int(self.cleaned_data['weight'])

        return weight


class QueryProductsForm(forms.Form):


    categories = Categories.objects.all()
    products = Products.objects.all()

    cats = []
    prices = []
    prices.append(
        ('$0-$10', '$0-$10')
    )
    prices.append(
        ('$11-$30', '$11-$30')
    )
    prices.append(
        ('$31-$50', '$31-$50')
    )
    prices.append(
        ('$51-$75', '$51-$75')
    )
    prices.append(
        ('$76-$100', '$76-$100')
    )
    prices.append(
        ('$101-$200', '$101-$200')
    )
    prices.append(
        (6, '$201+')
    )
    for c in categories:
        cats.append(
            (c.id, c.name)
        )

    category = forms.MultipleChoiceField(

        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=cats,

    )
    price = forms.MultipleChoiceField(

        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=prices,
        initial=None
    )
    keyword = forms.CharField(initial=None, required=False)

    def clean_keyword(self):

        keyword = self.cleaned_data['keyword']

        if ' ' in keyword:
            raise ValidationError(_('Please Enter a single keyword'))

        return keyword

    def clean_category(self):

        category = self.cleaned_data['category']

        return category

    def clean_price(self):

        price = self.cleaned_data['price']

        return price


class PurchaseProductForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()
    card_number = forms.CharField()
    security_number = forms.CharField()

    def clean_first_name(self):

        first_name = self.cleaned_data['first_name']

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        return last_name

    def clean_address(self):

        address = self.cleaned_data['address']

        return address

    def clean_card_number(self):

        card_number = self.cleaned_data['card_number']

        return card_number

    def clean_security_number(self):

        security_number = self.cleaned_data['security_number']

        if len(security_number) > 3:
            raise ValidationError(_("CVV number cannot exceed 3 digits"))

        return security_number

class AddEmployeeForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    job_role = forms.CharField()
    phone_number = forms.CharField()
    address = forms.CharField()
    email_address = forms.CharField()
    sex = forms.CharField()

    def clean_username(self):

        uname = self.cleaned_data['username']

        unames = Users.objects.values_list('username')

        for i in range(len(unames)):
            if uname == unames[i][0]:
                raise ValidationError(_('username already exists'))

        return uname

    def clean_password(self):

        pword = self.cleaned_data['password']

        return pword

    def clean_first_name(self):

        fn = self.cleaned_data['first_name']

        return fn

    def clean_last_name(self):

        ln = self.cleaned_data['last_name']

        return ln

    def clean_email_address(self):

        email_address = self.cleaned_data['email_address']

        return email_address

    def clean_address(self):

        addr = self.cleaned_data['address']

        return addr

    def clean_sex(self):

        sex = self.cleaned_data['sex']

        return sex

    def clean_job_role(self):

        job_role = self.cleaned_data['job_role']

        return job_role

    def clean_phone_number(self):

        phone_number = self.cleaned_data['phone_number']

        return phone_number

