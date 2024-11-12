# OC-Projet2 : Utilisez les bases de Python pour l'analyse de marché.

Ce programme permet la mise en place d'un pipeline ETL pour récupérer les informations de chaque produit répertorié sur le site [Books To Scrape](https://books.toscrape.com/).
Les informations récupérées sont mises en forme et injectées dans un fichier au format .csv :

- l'URL de la page produit
- le code UPC de chaque produit
- le titre
- le prix hors taxes
- le prix taxes incluses
- la quantité disponible
- la description
- la catégorie d'ouvrage
- le nombre de recommandations
- l'URL de l'image du produit

Ce programme récupère également les fichiers image de chaque produit qui seront enregistrés dans un dossier Images.

> [!NOTE]
> Ce programme n'effectue pas de surveillance des prix en temps réel.

## Prérequis

Pour installer et exécuter ce programme, vous aurez besoin d'une connexion internet.

Python doit être installé sur votre ordinateur (version 3.12.7 ou supérieur).

L'installateur **pip** doit également être disponible sur votre machine pour installer les dépendances.

## Installation et exécution du programme

<details>
<summary>Etape 1 - Installer git</summary><br>

Pour télécharger ce programme, vérifiez que git est bien installé sur votre poste.<br>
Vous pouvez l'installer en suivant les instructions fournies sur le site [git-scm.com](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

</details>

<details>
<summary>Etape 2 - Cloner le dépôt contenant le programme</summary><br>


Utilisez la commande suivante :

``git clone https://github.com/Guillaume-GG35/OC-Projet2.git``

</details>

<details>
<summary>Etape 3 - Créer et activer un evironnement virtuel</summary><br>

Placez vous dans le dossier **00_Livrables** et créez un environnement virtuel avec la commande ``python -m venv env``<br>
Activez cet environnement avec la commande ``source env/bin/activate``

</details>

<details>
<summary>Etape 4 - Installer les dépendances</summary><br>

Pour que ce programme s'exécute, vous aurez besoin des packages **requests** et **bs4** <br>
Exécutez la commande ``pip install requests bs4``

</details>

<details>
<summary>Etape 5 - Créer un dossier Images</summary><br>

Dans le dossier **00_Livrables**, créer un nouveau dossier nommé **Images**

</details>

<details>
<summary>Etape 6 - Exécuter le programme</summary><br>

Exécutez la commande ``python main.py``

</details>

## Fontionnement du programme

Les données seront extraites dans un fichier output_scraper.csv qui sera automatiquement créé par le programme dans le dossier **00_Livrables**.

Les images seront téléchargées et enregistrées dans le dossier **00_Livrables/Images** que vous avez créé précédemment.

> [!NOTE]
> Le programme peut prendre plusieurs minutes pour réaliser l'extraction des données.
