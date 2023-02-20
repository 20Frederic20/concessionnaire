from django.urls import path
from . import views


app_name = 'marque'


urlpatterns = [
	# post views
	path('<int:pk>/', views.MarqueDetailView.as_view(), name='detail'),
	path('', views.MarqueListView.as_view(), name='list'),
	path('add/', views.MarqueCreateView.as_view(), name='add'),
	path('update/<int:pk>/', views.MarqueUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', views.MarqueDeleteView.as_view(), name="delete"),
]