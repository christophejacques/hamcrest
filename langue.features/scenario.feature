# fichier: langue.features/scenario.feature
# language: fr
Fonctionnalité: Utiliser un navigateur

  Specification du contexte des tests

  Scénario: Ouvrir une page web

    Etape: Ouvrir le navigateur

      Quand j'ouvre le navigateur
      Alors je me rends sur la page web "https://www.example.com"
      Alors la page web est ouverte

  Scénario: Fermer une page web

    Etape: Fermer le navigateur

      Soit un utilisateur admin
      Etant donné Le navigateur est ouvert sur le site "https://www.example.com"
      Et L'utilisateur est connecte
      Lorsque l'utilisateur est connecte au site "https://www.example.com"
      Alors se deconnecter
      Et afficher un message

