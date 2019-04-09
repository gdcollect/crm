# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

import datetime


import sys
reload(sys)
sys.setdefaultencoding('utf8')


type_choice = (
    ('laptop','Laptop'),
    ('desktop','Desktop'),
    ('tameiakh','Ταμειακή Μηχανή'),
    
    )

tmhma_choice = (
    ('1','Οικονομική'),
    ('2','Τεχνική'),
    ('3','Διοικητική'),
    ('4','Γραφείο Προσωπικού'),
    ('5','Μισθοδοσία'),
    ('6','Γραφείο Δημάρχου'),
    ('7','Τμήμα Πληροφορικής'),
    ('8','Ληξιαρχείο')
    )

job_choice = (
    ('TeamViewer','TeamViewer'),
    ('Επίσκεψη','Επίσκεψη'),
    ('Γραφείο','Γραφείο')
    )

employee_choice = (
    ('1','Αλέξης Μαυραγάνης'),
    ('2','Γιώργος Μαυραγάνης'),
    ('3','Κωστής Βυτινιώτης'),
    ('4','Αθανασία Καρακούση'),
    ('5','Κώστας Βυτινιώτης')
    )

adeia_choice = (
    ('1','Κανονική'),
    ('2','Αναρρωτική'),
    ('3','Εορταστική')
    )

app_choice = (
    ('ΤΑΠ','ΤΑΠ'),
    ('Μισθοδοσία','Μισθοδοσία'),
    ('Διαχείριση Προσωπικού','Διαχείριση Προσωπικού'),
    ('Λογιστική','Λογιστική'),
    ('Μητρώο Πολιτών','Μητρώο Πολιτών'),
    ('Ύδρευση','Ύδρευση'),
    ('Πρωτόκολλο','Πρωτόκολλο'),
    ('Διαύγεια','Διαύγεια'),
    ('Έσοδα','Έσοδα'),
    ('Κοιμητήρια','Κοιμητήρια'),
    ('ΚΟΚ','ΚΟΚ'),
    ('Δημοτικός φόρος','Δημοτικός φόρος'),
    ('Site','Site'),
    ('Πρακτικό','Πρακτικό'),
    )

class Dhmos(models.Model):
    name = models.CharField(max_length=100,verbose_name='Πελάτης', blank=False)
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    fax = models.CharField(max_length=50, verbose_name='Fax', blank=True)
    teamviewer = models.CharField(max_length=60, verbose_name='TeamViewer', blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=250, blank=True, null=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)
    

    class Meta:
        verbose_name = 'Πελάτες'
        verbose_name_plural = 'Πελάτες'
        ordering = ['id']
    def __str__(self):
                return self.name



class Employee(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Δήμος', null=True)
    firstname = models.CharField(max_length=150, verbose_name='Όνομα', null=True)
    lastname = models.CharField(max_length=150, verbose_name='Επώνυμο', null=True)
    tmhma = models.CharField(max_length=100, choices= tmhma_choice, verbose_name='Υπηρεσία', blank=True)
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο', blank=False)
    cellphone = models.CharField(max_length=30, verbose_name='Κινητό', blank=True)
    email = models.EmailField(blank=True)
    info = models.TextField(max_length=1000, verbose_name='Πληροφορίες', blank=True)

    class Meta:
        verbose_name = 'Στοιχεία Επικοινωνίας Πελατών'
        verbose_name_plural = 'Στοιχεία Επικοινωνίας Πελατών'
        
    def __str__(self):
                return self.lastname




class Service(models.Model):
    employee = models.ForeignKey('auth.User', verbose_name='Χρήστης', on_delete=models.CASCADE) 
    customername = models.CharField(max_length=150, verbose_name='Ονομα Πελάτη', null=False,blank=True)#first last
    phone = models.CharField(max_length=100, verbose_name='Τηλέφωνο Σταθερό', null=True,blank=True)
    cellphone = models.CharField(max_length=100, verbose_name='Κινητό Τηλέφωνο', null=True, blank=True)
    modelinfo = models.CharField(max_length=150,choices=type_choice, verbose_name='Τύπος', null=True,blank=True)
    serialnumber = models.CharField(max_length=100, verbose_name='S/N', null=True,blank=True)
    modeltype = models.CharField(max_length=150, verbose_name='Μοντέλο', null=True,blank=True)
    importdate = models.CharField(max_length=150,verbose_name='Ημ. Εισαγωγής',blank=True)
    info = models.TextField(max_length=500, verbose_name='Διάγνωση',null=True,blank=True)
    exportdate = models.CharField(max_length=150,verbose_name='Ημ. Παράδοσης',blank=True)
    cost = models.IntegerField(verbose_name='Κόστος επισκευής',blank=True)
    year = models.CharField(max_length=50, verbose_name='Έτος', null=False,blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
                return self.customername



class Ergasies(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Πελάτης', default='-')
    importdate = models.DateField(verbose_name='Ημ. Κατ.')
    app = models.CharField(max_length=100, choices=app_choice,verbose_name='Εφαρμογή', blank=True)
    jobtype = models.CharField(max_length=100, choices=job_choice, verbose_name='Τύπος Εργασίας', default='TeamViewer')
    info = models.TextField(max_length=1000, verbose_name='Περιγραφή')
    text = models.TextField(max_length=1000, verbose_name='Σημειώσεις', blank=True)
    employee = models.ForeignKey('auth.User', max_length=100,  verbose_name='Υπάλληλος', default='-')#delete kai 
    time = models.CharField(max_length=20,verbose_name='Διάρκεια', default=0)
    name = models.CharField(max_length=100, verbose_name='Υπάλληλος Επικοιν.', null=True,help_text='Επώνυμο-Όνομα', blank=True)
    ticketid = models.CharField(max_length=50,verbose_name='Αίτημα OTS', blank=True)

    class Meta:
        verbose_name = 'Εργασίες'
        verbose_name_plural = 'Εργασίες'
        ordering = ['importdate']



class Aithmata(models.Model):
    dhmos = models.ForeignKey('Dhmos', on_delete=models.CASCADE, verbose_name='Δήμος')
    importdate = models.CharField(max_length=100,verbose_name='Ημ. Καταχώρησης')
    info = models.TextField(max_length=500, verbose_name='Περιγραφή')
    employee = models.CharField(max_length=100, verbose_name='Όν. Υπαλλήλου')
    assign = models.ForeignKey('auth.User', max_length=100, verbose_name='Χρέωση')
    closedate = models.CharField(max_length=100,verbose_name='Ημ. Κλεισίματος')

    class Meta:
        verbose_name = 'Αιτήματα'
        verbose_name_plural = 'Αιτήματα'


class Adeia(models.Model):
    employee = models.ForeignKey('auth.User',max_length=100, verbose_name='Υπάλληλος')
    adeiatype = models.CharField(max_length=50, choices=adeia_choice, verbose_name='Τύπος Άδειας', blank=True, default='-' )
    startdate = models.CharField(max_length=100,verbose_name='Από')
    enddate = models.CharField(max_length=100,verbose_name='Έως')
    createddate = models.CharField(max_length=100,verbose_name='Ημ. Δημουργίας')

    class Meta:
        verbose_name = 'Άδειες'
        verbose_name_plural = 'Άδειες'

   
    



