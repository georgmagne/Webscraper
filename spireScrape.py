# Scapes spireglede.no for data about microgreensseeds.

# Placeholder.html should be downloaded beforehand
# This is to not make alot of unusual requests to the webserver.
# Good choice to download html files is CURL in the commandline

from bs4 import BeautifulSoup
import requests
import csv


# Creating a .csv to write data to.
csv_file = open("sp_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Produkt", "Pris"])

# Creating parsable html file from already downloaded .html
with open("fro.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# Navigating the .html to find the relevant data.
# Hardcoded for this website.

# Finding link to wanted items
nav = soup.find("nav", class_="nav-side main-nav")
hrefs = nav.find_all("a") # List with <a href="...">

# Finding links to the relevant items
# Later goes to link and get info about item. (Price, quantity).
links = [] # Container for corrent link strings.
for elem in hrefs:
    # Removes irrelevant char, correct link string left.
    string = str(elem)[9:]
    link = ""
    for char in string:
        if char == "\"":
            break
        link += char

    if "fro" in link:
        links.append(link)

for link in links[2:]:
    link_string = "https://spireglede.no" + link
    src = requests.get(link_string).text
    soup = BeautifulSoup(src, "lxml")

    articles = soup.find_all("article")
    for article in articles:
        name = article.h3.text
        print(name)
        price = article.find("div", class_="offers")
        price = price.find("span", class_="price__display").text

        csv_writer.writerow([name, price])
