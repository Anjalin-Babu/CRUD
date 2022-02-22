from django.forms import ModelForm
from .models import Employee
class Employee_form(ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','mobile','emp_code','position')
        labels= {'fullname':'Full Name',
                'emp_code':'Employee Code',
                'mobile':'Mobile Number',
                'position':'Job Position'
                }