#!/usr/bin/env python3

""" Fonction permettant la création d'un objet 'soup' et prenant comme paramètre une adresse url """

import requests
from bs4 import BeautifulSoup

def link_to_parse(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup