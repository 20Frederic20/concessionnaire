from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Ceci est le nom de l'app qaund on veut appeler les diiefrents urls qu'il contient
app_name='utilisateurs'

urlpatterns = [
	# post views
	path('', views.dashboard, name='dashboard'),
	path('edit/', views.edit, name='edit'),
	path('login/', auth_views.LoginView.as_view(template_name="Utilisateurs/login.html"), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name="Utilisateurs/logout.html"), name='logout'),
	path('register/', views.RegistrationView.as_view(), name="register"),
	path('register_done/', views.RegistrationDone.as_view(), name="register_done"),

	path('password_change/', auth_views.PasswordChangeView.as_view(template_name="Utilisateurs/password_change.html"), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="Utilisateurs/password_change_done.html"), name='password_change_done'),

	path('password_reset/', auth_views.PasswordResetView.as_view(template_name="Utilisateurs/password_reset.html"), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="Utilisateurs/password_reset_done.html"), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Utilisateurs/password_reset_confirm.html"), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="Utilisateurs/password_reset_complete.html"), name='password_reset_complete'),
]