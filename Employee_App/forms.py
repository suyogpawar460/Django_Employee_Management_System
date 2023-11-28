# Procedure for using forms.Form
'''
1. import the django forms module
2. create the userdefined form class using predefined Form class
3. Creating userdefined form class fileds with form field classNames
'''

from django import forms


class EmployeeForm(forms.Form):
    ename = forms.CharField()
    salary = forms.FloatField()
    city = forms.CharField()


# Procedure for using forms.ModelForm
'''
1. import the django forms module
2. importing the required model class
3. create the userdefined modelform class using predefined ModelForm class
4. Creating one Meta class as nested class to this Userdefined class 
'''

from django import forms
from Employee_App.models import Employee


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ['ename','salary','city']
