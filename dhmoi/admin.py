# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Dhmos, Employee, Service, Ergasies, Aithmata, Adeia
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from import_export import fields,resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget,CharWidget

class DhmosinfoResource(resources.ModelResource):
	
	class Meta:
		model = Dhmos

class DhmosAdmin(ImportExportModelAdmin):
	resource_class = DhmosinfoResource
	list_display = ('name', 'phone', 'teamviewer', 'fax', 'email')
	list_filter = ['name',]
	search_fields = ['name',]
	

class EmployeeResource(resources.ModelResource):

	class Meta:
		model = Employee


class EmployeeAdmin(ImportExportModelAdmin):
	list_display = ('dhmos','lastname', 'firstname', 'phone', 'email' )
	search_fields = ['lastname',]
	

class ErgasiesResource(resources.ModelResource):
	dhmos = fields.Field(column_name='Δήμος',attribute='dhmos',widget=ForeignKeyWidget(Dhmos, 'name'))
	employee = fields.Field(column_name='Υπάλληλος', attribute='employee', widget=ForeignKeyWidget(User, 'last_name')) 
	jobtype = fields.Field(column_name='Τύπος', attribute='jobtype')
	importdate = fields.Field(column_name='Ημ. Καταχ.', attribute='importdate')
	app = fields.Field(column_name='Εφαμογή', attribute='app')
	info = fields.Field(column_name='Εργασία', attribute='info')
	name = fields.Field(column_name='Υπάλληλος Δήμου', attribute='name')
	time = fields.Field(column_name='Χρόνος', attribute='time')
	class Meta:
		model = Ergasies
		exclude =('id','text','ticketid')
		export_order = ('dhmos','importdate','app','employee','jobtype','info','name','time')
 		


class ErgasiesAdmin(ImportExportModelAdmin):
	list_display = ('dhmos','app','importdate','name','jobtype','info','employee','time','ticketid')
	search_fields = ['dhmos',]
	list_filter = ['employee','dhmos']
	ordering = ['importdate']
	resource_class = ErgasiesResource

class AdeiesResource(resources.ModelResource):

	class Meta:
		model = Adeia


class AdeiesAdmin(ImportExportModelAdmin):
	list_display = ('employee', 'adeiatype','startdate','enddate','createddate')
	search_fields = ['employee']
	list_filter = ['employee']

	



admin.site.register(Dhmos, DhmosAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Ergasies, ErgasiesAdmin)
admin.site.register(Service)
admin.site.register(Aithmata)
admin.site.register(Adeia, AdeiesAdmin)







admin.site.unregister(Group)
admin.site.site_header = "Μαζιώτης Σταύρος & ΣΙΑ ΕΕ"
admin.site.site_title = "Μαζιώτης Σταύρος & ΣΙΑ ΕΕ"
admin.site.index_title = "ACS Services"



