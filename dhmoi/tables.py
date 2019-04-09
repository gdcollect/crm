# -*- coding: utf-8 -*-
import django_tables2 as tables
from .models import Dhmos, Service, Ergasies, Aithmata, Employee, Adeia
from table import Table
from table.columns import Column


class DhmosinfoTable(tables.Table):
	class Meta:
		model = Dhmos
		template_name = 'django_tables2/bootstrap.html'
		fields = ('id', 'name', 'phone', 'fax', 'teamviewer','email', 'website',)
		
		#exclude = ()



class ServiceTable(tables.Table):
	class Meta:
		model = Service
		template_name = 'django_tables2/bootstrap.html'
		fields = ('id', 'customername', 'phone', 'cellphone', 'importdate', 'exportdate', 'year', 'info','cost')



class ErgasiesTable(tables.Table):

	class Meta:
		model = Ergasies
		template_name = 'django_tables2/bootstrap.html'
		fields = ('importdate','app',  'dhmos','name', 'jobtype', 'info', 'employee', 'time', 'ticketid')
		


class AithmataTable(tables.Table):
	class Meta:
		model = Aithmata
		template_name = 'django_tables2/bootstrap.html'
		fields = ('importdate','dhmos','info','employee','assign','closedate')






class EmployeeTable(Table):
    dhmos = Column(field='dhmos', header='Πελάτης')
    firstname = Column(field='firstname', header='Ονομα')
    lastname = Column(field='lastname', header='Επώνυμο')
    tmhma = Column(field='tmhma', header='Τμήμα')
    phone = Column(field='phone', header='Τηλέφωνο')
    cellphone = Column(field='cellphone', header='Κινητό')
    email = Column(field='email',header='E-mail')
    
    class Meta:
    	model = Employee
    	

class AdeiaTable(tables.Table):
	class Meta:
		model = Adeia
		template_name = 'django_tables2/bootstrap.html'
		fields = ('employee','adeiatype','startdate','enddate','createddate')
     