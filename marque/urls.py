from django.urls import path
from . import views


app_name = 'marque'


urlpatterns = [
	# post views
	path('<int:pk>/', views.MarqueDetail.as_view(), name='detail'),
	path('', views.MarqueList.as_view(), name='list'),
]