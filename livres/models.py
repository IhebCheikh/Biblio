from django.db import models
from datetime import date

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    date_publication = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} par {self.auteur}"


class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='emprunts')
    nom_emprunteur = models.CharField(max_length=255)
    date_emprunt = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.nom_emprunteur} a emprunté {self.livre.titre}"

class Album(models.Model):
    myimage = models.ImageField(upload_to='uploads/')