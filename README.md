# Integration-continue-app-flsak

# Application flask déployer sur Heroku 

--> Formation EPSI : **Intégration continue**



## Téléchargement du projet

```bash
git clone https://github.com/Mickevin/Integration-continue-app-flsak.git

cd Integration-continue-app-flsak

```


## Installation

Installez les dépendances suivantes pour lancer l'application Flask

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Démarage de l'application

Exécutez la commande suivante puis accédez à l'url suivante depuis un navigateur : http://127.0.0.1:4000

```bash
python app.py
```

## Arborescence du dossier

Détail des repertoires et des fichier contenus dans le dossier **Integration-continue-app-flsak**

* static/         : Répertoire contenant les pages html du projet => index.html(page d'acceuil), submit.html(page de confirmation du formulaire)

  |---> index.html

  |---> submit.html
  
<br>

* templates/     : Répertoire contenant les templates css et js du projet ainsi que les images (assets).

  |---> assets/

  |---> css/

  |---> js/
  
<br>

* tests/            : Répertoire contenant les tests unitaires à compléter.

  |---> test.py     
 
<br> 

* requirements.txt  : Dépendances python nécessaires au fonctionnement de l'application.

* README.md         : Fichier de présentation de l'application.

* Procfile          : Fichier permettant le déploiement de l'application sur la plateforme Heroku --> [Application déployée](vhttps://dashboard-app-epsi.herokuapp.com/)

* utiles.py         : Fichier python contenant l'ensemble des fonctions utiles au bon fonctionnement de l'application.

* app.ipynb         : Notebook de l'application flask, utile pour essayer son code dans une environement jupyter.

* app.py            : Application Flask principale



## Crédits
[Kévin Duranty](https://xn--kvin-duranty-beb.fr/)
<br>
[Thème Bootstrap de référence](https://startbootstrap.com/theme/freelancer)
