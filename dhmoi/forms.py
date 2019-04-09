# -*- coding: utf-8 -*-
from django import forms
from .models import Ergasies, Dhmos, Employee, Service, Aithmata, Adeia
from django.contrib.auth.models import User
from django.forms import ModelChoiceField



class NameChoiceField(ModelChoiceField):

    def label_from_instance(self,obj):
        return '{lastname} {firstname}'.format(lastname=obj.lastname, firstname=obj.firstname)
        
class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return '{last_name} {first_name}'.format(last_name=obj.last_name, first_name=obj.first_name)

class ErgasiaForm(forms.ModelForm):
    #name = forms.ModelChoiceField(required=False, queryset = Employee.objects.all().order_by('lastname'))
    
    name = NameChoiceField(queryset=Employee.objects.order_by('lastname'),label='Υπάλληλος Επικοιν.', required=False)
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name'), label='Υπάλληλος ACS')
    class Meta:
        
        model =  Ergasies
        fields = '__all__'
        fields = ['importdate','app','dhmos','name','jobtype','info','text','employee','time','ticketid']
        
  



class DhmosForm(forms.ModelForm):

    class Meta:
        model = Dhmos
        fields = '__all__'


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class AithmataForm(forms.ModelForm):
    assign = UserModelChoiceField(queryset=User.objects.order_by('last_name'), label='Χρέωση')
    class Meta:
        model = Aithmata
        fields = '__all__'


class ServiceForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name'), label='Υπάλληλος ACS')
    class Meta:
        model = Service
        fields = '__all__'


class AdeiaForm(forms.ModelForm):
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name'), label='Υπάλληλος ACS')
    class Meta:
        model = Adeia
        fields = '__all__'