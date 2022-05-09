from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url_scraper = "https://www.olx.ro/d/casa-gradina/"

request_page = urlopen(url_scraper)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

garden_items = html_soup.select("div[data-cy='l-card']")
# print(garden_items)

filename = 'produse.csv'
f = open(filename, "w", encoding="utf-8")

headers = "Categorie, Titlu , Pret , Descriere\n"

f.write(headers)
    
def filtru_Aspirator(s):
    return re.search("[aA][sS][pP][iI][rR][aA][tT][oO][rR]", s)


def filtru_Planta(s):
    return re.search("[pP][lL][aA][nN][tT][aA]", s)


def filtru_Mobila(s):
    return re.search("[mM][oO][bB][iI][lL][aA]", s)


def filtru_Garduri(s):
    return re.search("[gG][aA][rR][dD][uU][rR][iI]", s)


def filtru_Usi(s):
    return re.search("[uU][sS][iI]", s)


def filtru_Birou(s):
    return re.search("[bB][iI][rR][oO][uU]", s)


def filtru_Capac(s):
    return re.search("[cC][aA][pP][aA][cC]", s)


def filtru_Aparat(s):
    return re.search("[aA][pP][aA][rR][aA][tT]", s)


def filtru_Rigole(s):
    return re.search("[rR][iI][gG][oO][lL][eE]", s)


def filtru_Tigaie(s):
    return re.search("[tT][iI][gG][aA][iI][eE]", s)


def filtru_Container(s):
    return re.search("[cC][oO][nN][tT][aA][iI][nN][eE][rR]", s)


plante, aspiratoare, mobila, garduri, usi, birouri, capace, aparate, rigole, tigaie, containere = [
], [], [], [], [], [], [], [], [], [], []

for gradina in garden_items:
    # print(gradina.prettify())
    # print()
   # print()
    titlu = gradina.select('h6', _class="css-v3vynn-Text eu5v0x0")[0].text
    pret = gradina.select('p', _class="css-l0108r-Text eu5v0x0")[0].text
    #print(titlu + ' , ' + pret)

    href = f"https://www.olx.ro{gradina.select('a')[0]['href']}"

    request_page2 = urlopen(href)
    page_html2 = request_page2.read()
    request_page2.close()

    html_soup2 = BeautifulSoup(page_html2, 'html.parser')

    descriere = html_soup2.select('div', _class="css-g5mtbi-Text")[0].text

    #print(titlu)
    if filtru_Aparat(titlu):
        aparate.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Aspirator(titlu):
        aspiratoare.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Birou(titlu):
        birouri.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Capac(titlu):
        capace.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Container(titlu):
        containere.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Garduri(titlu):
        garduri.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Mobila(titlu):
        mobila.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Planta(titlu):
        plante.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Tigaie(titlu):
        tigaie.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Rigole(titlu):
        rigole.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
    elif filtru_Usi(titlu):
        usi.append({
            'titlu': titlu,
            'pret': pret,
            'descriere': descriere
        })
#Categorie, titlu, pret, descriere
if aparate != []:
    for aparat in aparate:
        f.write(
            f'Aparate, {aparat["titlu"]}, {aparat["pret"]}, {aparat["descriere"]}')
if aspiratoare != []:
    for aspirator in aspiratoare:
        f.write(
            f'Aspiratoare, {aspirator["titlu"]}, {aspirator["pret"]}, {aspirator["descriere"]}')
if birouri != []:
    for birou in birouri:
        f.write(
            f'Aspiratoare, {birou["titlu"]}, {birou["pret"]}, {birou["descriere"]}')
if capace != []:
    for capac in capace:
        f.write(
            f'Aspiratoare, {capac["titlu"]}, {capac["pret"]}, {capac["descriere"]}')
if containere != []:
    for container in containere:
        f.write(
            f'Aspiratoare, {container["titlu"]}, {container["pret"]}, {container["descriere"]}')
if garduri != []:
    for gard in garduri:
        f.write(
            f'Aspiratoare, {gard["titlu"]}, {gard["pret"]}, {gard["descriere"]}')
if mobila != []:
    for piesa in mobila:
        f.write(
            f'Aspiratoare, {piesa["titlu"]}, {piesa["pret"]}, {piesa["descriere"]}')
if plante != []:
    for planta in plante:
        f.write(
            f'Aspiratoare, {planta["titlu"]}, {planta["pret"]}, {planta["descriere"]}')
if tigaie != []:
    for tigai in tigaie:
        f.write(
            f'Aspiratoare, {tigai["titlu"]}, {tigai["pret"]}, {tigai["descriere"]}')
if rigole != []:
    for rigola in rigole:
        f.write(
            f'Aspiratoare, {rigola["titlu"]}, {rigola["pret"]}, {rigola["descriere"]}')
if usi != []:
    for usa in usi:
        f.write(
            f'Aspiratoare, {usa["titlu"]}, {usa["pret"]}, {usa["descriere"]}')

f.close()
