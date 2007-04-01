from django.urls import path
from . import views


app_name = 'reviews'


urlpatterns = [
	# post views
	path('add/<int:voiture_id>/', views.createreview, name='create'),
	path('update/<int:review_id>/', views.updatereview, name='update'),
	path('delete/<int:review_id>/', views.deletereview, name="delete"),
]