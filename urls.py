from django.urls import path 

from  hrmsconf import views

app_name = "hrmsconf"





urlpatterns = [
	path('hrms/conf/', views.hrmsconf, name='hrmsconf'),
	path('generate/level/and/group/', views.generatelevelandgroup, name='generatelevelandgroup'),	
	path('hrms/conf/tab/<str:tab>', views.hrmsconftab, name='hrmsconftab'),	
	path('hrms/conf/request/set/<str:tab>/<str:level>', views.hrmsconfrequestset, name='hrmsconfrequestset'),								 													
]

