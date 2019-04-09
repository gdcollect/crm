from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.home),
	url(r'dhmos_new/$', views.dhmospost_new, name='dhmos_new'),
	url(r'employee/$', views.employee, name="employee"),
	url(r'employee_new/$', views.employee_new, name='employee_new'),
	url(r'aithmata/$', views.aithmata, name="aithmata"),
	url(r'aithmata_new/', views.aithmata_new, name='aithmata_new'),
	url(r'service/$', views.service, name="service"),
	url(r'service_new/', views.service_new, name='service_new'),
	url(r'ergasies/$', views.ergasies, name='ergasies'),
	url(r'ergasia_new/', views.ergasia_new, name='ergasia_new'),
	url(r'adeia/', views.adeia, name='adeia'),
	url(r'adeia_new/', views.adeia_new, name='adeia_new'),
	url(r'update/ergasia/(?P<pk>\d+)/', views.ergasia_update, name='ergasia_update'),
	url(r'update/adeies/(?P<pk>\d+)/', views.adeia_update, name='adeia_update'),
	url(r'update/service/(?P<pk>\d+)/', views.service_update, name='service_update'),
	url(r'update/employee/(?P<pk>\d+)/', views.employee_update, name='employee_update'),
	url(r'update/dhmos/(?P<pk>\d+)/', views.dhmos_update, name='dhmos_update'),
	url(r'update/aithmata/(?P<pk>\d+)/', views.aithmata_update, name='aithmata_update'),
	url(r'delete/(?P<pk>\d+)/', views.delete_adeia, name='delete_adeia'),
	url(r'delete_aithmata/(?P<pk>\d+)/', views.delete_aithmata, name='delete_aithmata'),
	url(r'delete_employee/(?P<pk>\d+)/', views.delete_employee, name='delete_employee'),
	url(r'delete_ergasia/(?P<pk>\d+)/', views.delete_ergasia, name='delete_ergasia'),
	url(r'delete_home/(?P<pk>\d+)/', views.delete_home, name='delete_home'),
	url(r'delete_service/(?P<pk>\d+)/', views.delete_service, name='delete_service'),

]
#url(r'delete/(?P<pk>\d+)/', views.delete_adeia, name='delete_adeia'),