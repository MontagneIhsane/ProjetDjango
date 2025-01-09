from django.db import models

class Carte(models.Model):
    titre = models.CharField(max_length=255,default="Untitled")
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='livres_images/', blank=True, null=True)
    date_naissance = models.DateField()
    poste = models.CharField(max_length=200)
    equipe = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titre