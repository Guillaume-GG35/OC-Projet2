#!/usr/bin/env python3

""" Ce code permet l'extraction de tous les produits du site https://books.toscrape.com.

Il retourne un fichier csv contenant les éléments suivants :

url - l'URL de la page produit
upc - le code UPC du produit
title - le titre du produit
price_including_tax - le prix taxes incluses
price_excluding_tax - le prix hors taxes
number_available - la quantité disponible en stock
product_description - la description du produit
category - la catégorie d'ouvrage
review_rating - le nombre de commentaires
image_url - l'adresse url locale de l'image associée au produit """

import requests
import parser_url
import csv
from pathlib import Path
import os

import scraper_books

#Fontion permettant le téléchargement des images avec utilisation du hash pour dissocier les doublons
def download_image(image_url, image_file):
    if os.path.exists(image_file) == False :
        image = requests.get(image_url)
        with open(image_file, 'wb') as fichier_image: #Argument "wb" : écriture de données binaires
            fichier_image.write(image.content)

user_auth_rm_files = ""
images_dir = str(Path(__file__).resolve().parent) + "/Images"

if os.path.exists(images_dir) :
    while user_auth_rm_files != "Y" and user_auth_rm_files != "n" :
        user_auth_rm_files = input("Un dossier Images a été trouvé. Souhaitez-vous vider le dossier Images et importer à nouveau tous les éléments? [Y/n] : ")
        if user_auth_rm_files != "Y" and user_auth_rm_files != "n" :
            print("Merci de répondre par 'Y' pour Oui ou 'n' pour Non.")
    if user_auth_rm_files == "Y" :
        for filename in os.listdir(images_dir) :
            os.remove(images_dir + "/" + filename)
        print("Le contenu du dossier Images a été supprimé. Les données vont être importées à nouveau.")
    else :
        print("Les images existantes ne seront pas écrasées.")
        print("Ecriture des données dans le fichier output_scraper.csv en cours...")

else :
    os.mkdir('Images')
    print("Le dossier Images a été créé.")
    print("Ecriture des données dans le fichier output_scraper.csv et téléchargement des images en cours...")
    
print("0 %")

i = 1

#Import des données de la page dont l'url est importée par scraper_books.py
for element in scraper_books.url_list:
    url = element
    soup = parser_url.link_to_parse(url)

    #Récupération d'une partie des données sous forme de dictionnaire
    table_scrap = soup.find_all("tr")
    table = {}

    for element in table_scrap:
        key = element.find("th").string
        value = element.find("td").string
        
        if key == "Product Type" or key == "Tax" :
            continue
        else: 
            table[key] = value

    #Insertion de chaque donnée dans sa variable
    upc = table["UPC"]

    title = soup.find("li", class_="active").string
    title_image = title
    while title_image.find("/") != -1: #La méthode find() ne retourne pas "false" mais "-1" si le caractère n'est pas trouvé
        title_image = title_image.replace("/", "-")

    price_including_tax = table ["Price (incl. tax)"]

    price_excluding_tax = table ["Price (excl. tax)"]

    number_available = ""
    for element in table["Availability"]:
        try:
            int(element)
            number_available += element
        except ValueError:
            continue
    number_available = int(number_available)

    
    if soup.find("p", class_="") == None:
        product_description = ""
    else:
        product_description = soup.find("p", class_="").string

    category_scrap = soup.find("ul", class_="breadcrumb")
    category_names = []

    for a in category_scrap.find_all("a"):
        category_names.append(a.string)

    category = category_names[-1]

    review_rating = int(table["Number of reviews"])

    image_tag = soup.find("img")
    image_src = image_tag["src"] #On accède à l'attribut "src" de la même facon qu'on afficherait une valeur de dictionnaire
    image_url = "https://books.toscrape.com/" + image_src[6:]
    image_hash = image_src[27:-4] #Récupération du hash présent dans le nom de fichier original

    image_file = os.path.join(images_dir + "/" + title_image + "-" + image_hash + ".jpg")

    download_image(image_url, image_file)

    #Ecriture des données dans le fichier output_scraper.csv
    data_csv = [url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_file]

    with open("output_scraper.csv", "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_ALL)
        writer.writerow(data_csv)

    i += 1
    nb_books = len(scraper_books.url_list)
    if i == int(nb_books * 0.25) :
        print("25 %")
    elif i == int(nb_books * 0.5) :
        print("50 %")
    elif i == int(nb_books * 0.75) :
        print("75 %")

print("100 %")
print("L'import des données est terminé !")