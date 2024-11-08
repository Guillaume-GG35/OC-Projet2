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
image_url - l'adresse url de l'image associée au produit """

import requests
import parser_url
import csv

import scraper_books

#Fontion permettant le téléchargement des images avec utilisation du hash pour dissocier les doublons
def download_image(image_url, title, hash):
    image = requests.get(image_url)
    if image == "":
        print("L'image associée à " + title + " n'a pas été trouvée.")
    while title.find("/") != -1: #La méthode find() ne retourne pas "false" mais "-1" si le caractère n'est pas trouvé
        title = title.replace("/", "-")
    with open("Images/" + title + "-" + hash + ".jpg", 'wb') as fichier_image: #Argument "wb" : écriture de données binaires
        fichier_image.write(image.content)

print("Ecriture des données dans le fichier output_scraper.csv en cours... Merci de patienter.")

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
    image_url = image_tag["src"] #On accède à l'attribut "src" de la même facon qu'on afficherait une valeur de dictionnaire
    image_hash = image_url[27:-4] #Récupération du hash présent dans le nom de fichier original
    
    download_image("https://books.toscrape.com/" + image_url[6:], title, image_hash)

    #Ecriture des données dans le fichier output_scraper.csv
    data_csv = [url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]

    with open("output_scraper.csv", "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        writer.writerow(data_csv)

print("L'import des données est terminé !")