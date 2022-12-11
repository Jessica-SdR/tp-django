from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=50, default=None, blank=True, null=True)
    prenom = models.CharField(max_length=30, default=None, blank=True, null=True)
    telephone = models.CharField(max_length=14, default=None, blank=True, null=True)
    entreprise = models.BooleanField(default=False, null=False)