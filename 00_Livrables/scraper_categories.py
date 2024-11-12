#!/usr/bin/env python3

""" Ce code permet l'extraction d'une liste d'url des différentes catégories d'ouvrages du site https://books.toscrape.com. """

import parser_url
import csv
import os
from pathlib import Path

directory = str(Path(__file__).resolve().parent)

user_auth_rm_csv = ""

if os.path.exists(directory + "/output_scraper.csv") :
    while user_auth_rm_csv != "Y" and user_auth_rm_csv != "n" :
        user_auth_rm_csv = input("Le fichier output_scraper.csv existe déja. Souhaitez-vous l'effacer et relancer l'import de données? [Y/n] : ")
        if user_auth_rm_csv != "Y" and user_auth_rm_csv != "n" :
            print("Merci de répondre par 'Y' pour Oui ou 'n' pour Non.")

if user_auth_rm_csv == "n" :
    print("Fin de programme !")
    exit()

#Création du fichier output_scraper.csv et écriture de la ligne d'en-tête
with open("output_scraper.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=";", quoting=csv.QUOTE_ALL)
    header_csv = ["product_page_url", "universal_product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    writer.writerow(header_csv)
    
print("Le fichier output_scraper.csv a été initialisé avec succès !")
print("Extraction de la liste des catégories...")

soup = parser_url.link_to_parse("https://books.toscrape.com/")

category_links = []

scraped_categories = soup.find("ul", class_="nav-list")
a_tag = scraped_categories.find_all("a")

i = 0

for element in a_tag :
    if i == 0:
        i += 1
        continue
    url = element["href"]
    category_links.append("https://books.toscrape.com/" + url)

print("Les liens des catégories ont été récupérés avec succès !")