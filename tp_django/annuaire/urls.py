from annuaire.views import *
from django.urls import path


urlpatterns = [
    path('annuaire/', liste, name="annuaire"),
    path('annuaire/particulier/', liste_particulier, name="pages_blanches"),
    path('annuaire/entreprise/', liste_entreprise, name="pages_jaunes"),
    path('annuaire/contact/<nom>', contact, name="contact"),
]