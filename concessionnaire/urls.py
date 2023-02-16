"""concessionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from voiture import views as voiture_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', voiture_views.VoitureView.as_view(), name='index'),
    path('assistance/', voiture_views.AssistanceView.as_view(), name='assistance'),
    path('concession/', voiture_views.ConcessionView.as_view(), name='concession'),
    path('voiture/', include('voiture.urls', namespace='voiture')),
    path('marque/', include('marque.urls', namespace='marque')),
    #path('__debug__/', include('debug_toolbar.urls')),
    path('utilisateurs/', include('utilisateurs.urls', namespace='utilisateurs')),
] 


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
On utilise souvent un nom pour les apps quand on écrit plusieurs applications
et dont les noms des urls spnt les memes. Alors les app_namme permettent de se
rediriger vers cet url selin de nom de l'app defini
'''