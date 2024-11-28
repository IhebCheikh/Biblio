from django.contrib import admin
from .models import Livre, Emprunt

# Enregistrer le modèle Livre
@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication', 'disponible')  # Colonnes affichées
    list_filter = ('disponible', 'date_publication')  # Filtres latéraux
    search_fields = ('titre', 'auteur')  # Barre de recherche
    ordering = ('titre',)  # Tri par défaut (par titre)

# Enregistrer le modèle Emprunt
@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('livre', 'nom_emprunteur', 'date_emprunt')  # Colonnes affichées
    list_filter = ('date_emprunt',)  # Filtres latéraux
    search_fields = ('nom_emprunteur', 'livre__titre')  # Barre de recherche
