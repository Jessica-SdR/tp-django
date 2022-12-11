from django.shortcuts import render
from annuaire.models import Contact

# Create your views here.
contacts = [
        {
            "nom": "Cassidy",
            "prenom": "Hammond",
            "telephone": "03 94 96 50 97"
            },
            {
            "nom": "Charde",
            "prenom": "Hyde",
            "telephone": "03 44 84 02 60"
            },
            {
            "nom": "Dorian",
            "prenom": "Bailey",
            "telephone": "03 78 24 49 97"
            },
            {
            "nom": "Vivien",
            "prenom": "Duffy",
            "telephone": "03 26 81 80 44"
            },
            {
            "nom": "Ivory",
            "prenom": "Colon",
            "telephone": "03 85 87 65 55"
            }
        ]

def liste(request):
    contacts = Contact.objects.all()
    return render(request, 'annuaire/list.html', context={"contacts": contacts})

def liste_particulier (request):
    contacts = Contact.objects.filter(entreprise=False)
    return render(request, "annuaire/pages_blanches.html", context={"contacts": contacts})

def liste_entreprise (request):
    contacts = Contact.objects.filter(entreprise=True)
    return render(request, "annuaire/pages_jaunes.html", context={"contacts": contacts})

def contact(request, nom):
    contact = Contact.objects.all().filter(nom=nom).first()
    print(contact) 
    # for contact in contacts:
    #     if contact["nom"] == nom:
    #         nomContact = contact["nom"]
    #         prenomContact = contact["prenom"]
    #         telContact = contact["telephone"]
    # context={"nom": nomContact, "prenom": prenomContact, "telephone":telContact}
    redirect = 'pages_jaunes' if contact.entreprise else 'pages_blanches'
    return render(request, "annuaire/contact.html", context={"contact":contact, "redirect":redirect})