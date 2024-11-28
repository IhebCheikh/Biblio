from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre, Album
from datetime import date
from .forms import LivreForm

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'livres/ajouter_livre.html', {'form': form})

def liste_livres(request):
    livres = Livre.objects.filter(disponible=True)
    return render(request, 'livres/liste_livres.html', {'livres': livres})

def details_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    return render(request, 'livres/details_livre.html', {'livre': livre})

def modifier_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if request.method == 'POST':
        livre.titre = request.POST.get('titre', livre.titre)
        livre.auteur = request.POST.get('auteur', livre.auteur)
        livre.date_publication = request.POST.get('date_publication', livre.date_publication)
        livre.disponible = request.POST.get('disponible', livre.disponible) == 'on'
        livre.save()
        return redirect('liste_livres')
    return render(request, 'livres/modifier_livre.html', {'livre': livre})

def livres_non_disponibles(request):
    livres = Livre.objects.filter(disponible=False)
    return render(request, 'livres/livres_non_disponibles.html', {'livres': livres})

from .models import Emprunt

def emprunter_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    if livre.disponible:
        if request.method == 'POST':
            nom_emprunteur = request.POST.get('nom_emprunteur')
            Emprunt.objects.create(livre=livre, nom_emprunteur=nom_emprunteur)
            livre.disponible = False
            livre.save()
            return redirect('liste_livres')
        return render(request, 'livres/emprunter_livre.html', {'livre': livre})
    return render(request, 'livres/erreur.html', {'message': 'Ce livre n\'est pas disponible.'})

def fct(request):
    res=Album.objects.all()

    return render(request,"index.html",{'res':res})