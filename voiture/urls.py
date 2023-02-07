from django.urls import path
from . import views


app_name = 'voiture'


urlpatterns = [
	# post views
	path('', views.VoitureList.as_view(), name='list'),
	path('add/', views.VoitureAdd.as_view(), name='add'),
	path('update/<int:pk>/', views.VoitureUpdate.as_view(), name='update'),
	path('delete/<int:pk>/', views.VoitureDelete.as_view(), name="delete"),
]