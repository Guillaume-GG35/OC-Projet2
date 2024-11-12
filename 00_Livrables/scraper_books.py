#!/usr/bin/env python3

""" Ce code permet l'extraction d'une liste d'url de Produits à partir d'une catégorie d'ouvrages du site https://books.toscrape.com. """

import parser_url
import scraper_categories

#Fonction permettant l'extraction de tous les livres d'une page
def extract_products_url():
    product_links = soup.find_all("article", class_="product_pod")

    for element in product_links:
        product_title = element.find("h3")
        a_tag = product_title.find("a")
        url_to_clean = a_tag["href"]
        cleaned_url = url_to_clean[9:]
        url_list.append("https://books.toscrape.com/catalogue/" + cleaned_url)

    return url_list

url_list = []

print("Extraction de la liste des ouvrages...")

#Boucle sur les éléments retournés par scraper_categories.py
for link in scraper_categories.category_links:
    soup = parser_url.link_to_parse(link)

    extract_products_url()

    #Vérification de l'existence d'un lien "next"
    i = 1
    next_link = soup.find("li", class_="next")

    #Exécution de la fonction extract_products_url() tant qu'il existe une page suivante
    while next_link != None:
        i += 1
        soup = parser_url.link_to_parse(link[0:-10] + "page-" + str(i) + ".html")
        extract_products_url()
        next_link = soup.find("li", class_="next")

print("Le site répertorie " + str(len(url_list)) + " ouvrages.")