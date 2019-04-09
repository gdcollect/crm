# -*- coding: utf-8 -*-
from .models import Employee, Dhmos, Aithmata, Ergasies
import django_filters
from django.contrib.auth.models import User











class EmployeeFilter(django_filters.FilterSet):
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Employee 
        fields = ['dhmos', 'firstname', 'lastname',]


class DhmosFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Dhmos 
        fields = ['name']


class AithmataFilter(django_filters.FilterSet):
    
    employee = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Aithmata
        fields = ['dhmos', 'employee', 'assign']


class ErgasiesFilter(django_filters.FilterSet):
    
    class Meta:
        model = Ergasies
        fields = ['dhmos','app','employee',]