# Scrapes hageglede.no for data about microgreensseeds.

# Slighty more refined version of spireScrape.py

from bs4 import BeautifulSoup
import requests
import csv
import re

csv_file = open("hage_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Produkt", "Pris"])

# Creating parsable html file
link = "https://hageglede.no/butikk/spiselige-vekster/mikrogront/mikrogront-fro/"
src = requests.get(link).text
soup = BeautifulSoup(src, "lxml")

# Finding link to wanted items
links = []
articles = soup.find_all("article")
for article in articles:

    string = str(article.a)
    ut = re.findall("href=\".*?\"", string)
    ut = ut.pop()
    ut = ut[6:-1]
    links.append(ut)

for link in links[1:]:
    src = requests.get(link).text
    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all("article")
    for article in articles:
        div = article.find_all("div", class_="offers")
        div = div[0]
        price = div.span.find_all("span", class_="price__display")[0].text
        name = article.a.h3.text
        print(name, price)
        csv_writer.writerow([name, price])
