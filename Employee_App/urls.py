
from django.urls import path
from Employee_App import views
# from Employee_App.views import home_view

urlpatterns = [
    path('home/', views.home_view, name='employee_home'),

    path('create/', views.createemployee_view, name='create_employee'),

    path('list/', views.employee_list_view, name='list_employee'),

    path('add_form/', views.CreateEmployee_FormView, name='add_form_employee'),
    path('add_modelform/', views.CreateEmployee_ModelFormView, name='add_modelform_employee'),

]
