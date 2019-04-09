# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django_tables2 import RequestConfig
from .models import Dhmos, Service, Ergasies, Aithmata, Employee, Adeia
from .tables import DhmosinfoTable, ServiceTable, ErgasiesTable, AithmataTable, EmployeeTable, AdeiaTable
from datetime import datetime
from datetime import timedelta
from .forms import ErgasiaForm, DhmosForm, EmployeeForm, AithmataForm, ServiceForm, AdeiaForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import EmployeeFilter, DhmosFilter, AithmataFilter, ErgasiesFilter




@login_required
def home(request):
    alldhmos=Dhmos.objects.all()
    dhmos_filter = DhmosFilter(request.GET, queryset=alldhmos)
    #context={'alldhmos':alldhmos}
    #table = DhmosinfoTable(Dhmos.objects.all(), order_by='id')
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/home.html', {'filter': dhmos_filter})

@login_required
def service(request):
    allservice=Service.objects.all()
    context={'allservice':allservice}
    #table = ServiceTable(Service.objects.all())
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/service.html',context)

@login_required
def ergasies(request):
    order_by = request.GET.get('order_by', '-importdate')
    allergasies=Ergasies.objects.all().order_by(order_by)
    ergasies_filter = ErgasiesFilter(request.GET, queryset=allergasies)
    #context={'allergasies':allergasies}
    #table = ErgasiesTable(Ergasies.objects.all(), order_by='importdate')
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/ergasies.html', {'filter': ergasies_filter})


@login_required
def aithmata(request):
    allaithmata=Aithmata.objects.all()
    aithmata_filter = AithmataFilter(request.GET, queryset=allaithmata)
    #context={'allaithmata':allaithmata}
    #table = AithmataTable(Aithmata.objects.all())
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/aithmata.html', {'filter':aithmata_filter})


@login_required
def employee(request):
    allemployees=Employee.objects.get_queryset().order_by('id')
    employee_filter = EmployeeFilter(request.GET, queryset=allemployees)
    #table = EmployeeTable()
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/employee.html',{'filter': employee_filter})


@login_required
def adeia(request):
    alladeies=Adeia.objects.filter(employee=request.user)
    context={'alladeies':alladeies}
    #table = AdeiaTable(Adeia.objects.all())
    #RequestConfig(request).configure(table)
    return render(request, 'dhmoi/adeies.html',context)




@login_required
def dhmospost_new(request):
    if request.method == "POST":
        form = DhmosForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        dhmosform = DhmosForm()
    return render(request, 'dhmoi/dhmos_new.html', {'dhmosform': dhmosform})

@login_required
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('employee')
    else:
        employeeform = EmployeeForm()
    return render(request, 'dhmoi/employee_new.html', {'employeeform': employeeform})

@login_required
def aithmata_new(request):
    if request.method == "POST":
        form = AithmataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('aithmata')
    else:
        aithmataform = AithmataForm()
    return render(request, 'dhmoi/aithmata_new.html', {'aithmataform': aithmataform})


@login_required
def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('service')
    else:
        form = ServiceForm()
    return render(request, 'dhmoi/service_new.html', {'serviceform': form})

@login_required
def ergasia_new(request):
    if request.method == "POST":
        form = ErgasiaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ergasies')
    else:
        form = ErgasiaForm(initial={'employee':request.user})
    return render(request, 'dhmoi/ergasia_new.html', {'form': form})

@login_required
def adeia_new(request):
    if request.method == "POST":
        form = AdeiaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('adeia')
    else:
        form = AdeiaForm(initial={'employee':request.user})
    return render(request, 'dhmoi/adeia_new.html', {'adeiaform': form})

@login_required
def ergasia_update(request, pk):
    post = get_object_or_404(Ergasies, pk=pk)
    if request.method == "POST":
        form = ErgasiaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('ergasies')
    else:
        form = ErgasiaForm(instance=post)
    return render(request, 'dhmoi/update/ergasia_update.html', {'form': form})

@login_required
def adeia_update(request, pk):
    post = get_object_or_404(Adeia, pk=pk)
    if request.method == "POST":
        form = AdeiaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('adeia')
    else:
        form = AdeiaForm(instance=post)
    return render(request, 'dhmoi/update/adeia_update.html', {'adeiaform': form})

@login_required
def service_update(request, pk):
    post = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('service')
    else:
        form = ServiceForm(instance=post)
    return render(request, 'dhmoi/update/service_update.html', {'serviceform': form})

@login_required
def employee_update(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('employee')
    else:
        form = EmployeeForm(instance=post)
    return render(request, 'dhmoi/update/employee_update.html', {'employeeform': form})

@login_required
def dhmos_update(request, pk):
    post = get_object_or_404(Dhmos, pk=pk)
    if request.method == "POST":
        form = DhmosForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('/')
    else:
        form = DhmosForm(instance=post)
    return render(request, 'dhmoi/update/dhmos_update.html', {'dhmosform': form})

@login_required
def aithmata_update(request, pk):
    post = get_object_or_404(Aithmata, pk=pk)
    if request.method == "POST":
        form = AithmataForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('aithmata')
    else:
        form = AithmataForm(instance=post)
    return render(request, 'dhmoi/update/aithmata_update.html', {'aithmataform': form})


#Δυνατότητα delete σε κάθε εγγραφή στους πίνακες
def delete_adeia(request,pk):
    object = Adeia.objects.get(pk=pk)
    object.delete()
    return redirect('adeia')

def delete_aithmata(request,pk):
    object = Aithmata.objects.get(pk=pk)
    object.delete()
    return redirect('aithmata')

def delete_employee(request,pk):
    object = Employee.objects.get(pk=pk)
    object.delete()
    return redirect('employee')

def delete_ergasia(requets,pk):
    object = Ergasies.objects.get(pk=pk)
    object.delete()
    return redirect('ergasies')

#home είναι η κεντρική σελίδα-δήμοι πληροφορίες
def delete_home(request,pk):
    object = Dhmos.objects.get(pk=pk)
    object.delete()
    return redirect('/')

def delete_service(request,pk):
    object = Service.objects.get(pk=pk)
    object.delete()
    return redirect('service')

