# fichier:features/francais.feature
# language: fr
Fonctionnalité: Utilisation de Firefox

    Contexte: Ouverture du Navigateur
        Etant donné le navigateur est ouvert (sinon l'ouvrir)

    Scénario: Ouverture Rcipac
        Lorsque je me rends sur la page web "https://rcipac.asp-public.fr/accueil"
        Alors la page web est ouverte
        Et l'utilisateur est connecte au site "https://rcipac.asp-public.fr/accueil"

    Scénario: Recherche Individu
        Etant donné l'utilisateur est connecte au site "https://rcipac.asp-public.fr/accueil"
        Lorsque je me rends sur la page web "https://alpha.asp-public.fr/recherche"
        Alors la page web est ouverte
        Et l'utilisateur est connecte au site "https://alpha.asp-public.fr/recherche"
        Et se deconnecter
