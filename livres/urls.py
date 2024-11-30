from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/<int:id>/', views.details_livre, name='details_livre'),
    path('livres/modifier/<int:id>/', views.modifier_livre, name='modifier_livre'),
    path('livres/non-disponibles/', views.livres_non_disponibles, name='livres_non_disponibles'),
    path('livres/emprunter/<int:id>/', views.emprunter_livre, name='emprunter_livre'),
    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),

    path('image/', views.fct, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
