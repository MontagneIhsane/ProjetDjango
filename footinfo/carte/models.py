from django.db import models

class Carte(models.Model):
    titre = models.CharField(max_length=255,default="Untitled")
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='livres_images/', blank=True, null=True)
    date_naissance = models.DateField()
    poste = models.CharField(max_length=200)
    equipe = models.CharField(max_length=100)

    def moyenne_notes(self):
        notes = self.note_set.all()  # Récupère toutes les notes associées à ce joueur
        if notes.exists():
            return round(sum(note.note for note in notes) / notes.count(), 2)
        return "Pas encore noté"
    
    def __str__(self):
        return self.titre

from django.contrib.auth.models import User

class Note(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur qui note
    joueur = models.ForeignKey(Carte, on_delete=models.CASCADE)  # Joueur noté
    note = models.IntegerField()  # Note donnée (par exemple, de 1 à 5)
    date = models.DateTimeField(auto_now_add=True)  # Date de la note

    class Meta:
        unique_together = ('utilisateur', 'joueur')  # Un utilisateur ne peut noter un joueur qu'une seule fois

    def __str__(self):
        return f"{self.utilisateur.username} -> {self.joueur.nom} : {self.note}"

from .models import Note

class Note(models.Model):
    joueur = models.ForeignKey('Carte', on_delete=models.CASCADE, related_name='notes')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    valeur = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Note: {self.valeur} pour {self.joueur.nom}"