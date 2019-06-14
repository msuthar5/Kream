from django.urls import path

from . import views

urlpatterns = [
    path('success/', views.index, name='index'),
    path('', views.login_controller, name='login-controller'),
    path('register/', views.registration_controller, name='registration-controller'),
    path('customer_info.html/', views.customer_info_controller, name="customer-info-controller"),
    path('<int:customer_id>/customer-view/', views.cust_view, name="cust-view"),
    path('<int:manager_id>/manager-view/', views.manager_view, name="manager-view"),
    path('<int:employee_id>/employee-view/', views.employee_view, name="employee-view"),
    path('<int:customer_id>/customer-view/add-product/', views.add_product_view, name='add-product-view'),
    path('<int:customer_id>/customer-view/query-view/', views.productQueryController, name='product-query-controller'),
    path('query-view/<int:product_id>/purchase-product/', views.purchase_product_controller, name='purchase-product-controller'),
    path('<int:customer_id>/customer-view/update-info/', views.update_info_controller, name="update-info-controller"),
    path('<int:manager_id>/manager-view/add-employee/', views.add_employee, name='add-employee'),
    path('<int:manager_id>/manager-view/warehouse-product-view/', views.managers_products, name='managers-products'),
    path('<int:admin_id>/admin-view/', views.admin_view, name='admin-view'),
    path('<int:admin_id>/admin-view/admin-customers/', views.admin_customers, name='admin-customers'),
    path('<int:admin_id>/admin-view/admin-managers/', views.admin_managers, name='admin-managers'),
    path('<int:admin_id>/admin-view/admin-employees/', views.admin_customers, name='admin-employees')

]
