from django.urls import path
from . import views


app_name = 'voiture'


urlpatterns = [
	# post views
	#path('', views.VoitureView.as_view(), name='index'),
	path('<int:pk>/', views.VoitureDetail.as_view(), name='detail'),
	path('list/', views.VoitureList.as_view(), name='list'),
	path('add/', views.VoitureAdd.as_view(), name='add'),
	path('search/', views.VoitureSearchView.as_view(), name='search'),
	path('update/<int:pk>/', views.VoitureUpdate.as_view(), name='update'),
	path('delete/<int:pk>/', views.VoitureDelete.as_view(), name="delete"),
	path('<int:pk>/achat/', views.VoitureAchat.as_view(), name='payement'),	
]