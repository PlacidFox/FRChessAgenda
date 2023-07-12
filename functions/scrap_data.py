from time import sleep
import json
import unidecode
import os
import datetime
import requests

from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from cli_display.cli_display import end_scrap, launch_scrap, print_page, print_page_find

#import const CADENCES
from functions.values import CADENCES
#import const SLEEP
from functions.values import SLEEP_TIME
# import path des fichiers JSON
from functions.values import jsonFiles
#import dictr des mois pour mapping
from functions.values import MONTH



# Crée le fichier db.JSON si n'est pas existant
def init_fetch_data():

    full_dicts_tournois = []
    
    for cadence in CADENCES:
        full_dicts_tournois = full_dicts_tournois + scrapping_script(cadence)

    dict_for_json = create_json_structure(full_dicts_tournois)
    
    write_database_json(dict_for_json, jsonFiles.FULL_JSON.value)
 
# Archive le fichier db.json (en old_db) puis créer le nouveau fichier db.json à jour
def maj_fetch_data():

    if os.path.exists(jsonFiles.OLD_FULL_JSON.value):
        os.remove(jsonFiles.OLD_FULL_JSON.value)
    os.rename(jsonFiles.FULL_JSON.value, jsonFiles.OLD_FULL_JSON.value)

    full_dicts_tournois = []

    for cadence in CADENCES:
        full_dicts_tournois = full_dicts_tournois + scrapping_script(cadence)

    dict_for_json = create_json_structure(full_dicts_tournois)

    write_database_json(dict_for_json, jsonFiles.FULL_JSON.value)


# Récupère les données des tournois d'une cadence et retourne un dict prêt à mettre en JSON
def scrapping_script(cadence):

    soup_tab =[]

    #pour cacher le navigateur ouvert par selenium
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE) #inutile ?

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    
    launch_scrap(cadence.name) # fonction afficahge avancement

    url_page = cadence.value

    driver.get(url_page)
    sleep(SLEEP_TIME)

    #calcul le nombre de page à scroller
    nb_pages = detect_nb_pages(driver)
    sleep(SLEEP_TIME)
    
    # execute la fonctions balayant chaque page et récupérant les datas de chaque soup
    soup_tab = scroll_pages(driver, nb_pages)
    
    end_scrap(cadence.name) # display fonctions

    # met en forme chaque soup dans un dict format JSON
    dicts_tournois = soup_to_dict(soup_tab, cadence, nb_pages) 

    sleep(SLEEP_TIME)
    driver.quit()

    #retourne les data pour le dict prete pour transfo en JSON
    return dicts_tournois



#Detecte le nb de pages à balayer pour la boucle for
def detect_nb_pages(driver):
    links = driver.find_elements_by_xpath("//*[@id=\"aspnetForm\"]/div[5]/table/tbody/tr/td")

    if len(links) == 0:
        print_page_find(1)
    else :
        print_page_find(len(links))

    return len(links)


#balaie chaque page et stock dans un tableau un objet BS4 (Soup) les données de chaque page
def scroll_pages(driver, nb_pages):

    soup_tab = []

    #gestion différente si une seule page car pas de liens à cliquer
    if nb_pages == 0:


        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        soup_tab.append(soup)
        print_page(1,1) # fonction d'affichage de l'avancement

        sleep(SLEEP_TIME)

        

    else:
        for i in range (1,nb_pages-1):

            links = driver.find_elements_by_xpath("//*[@id=\"aspnetForm\"]/div[5]/table/tbody/tr/td")
            links[i].click()
            sleep(SLEEP_TIME)

            page_source = driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")

            soup_tab.append(soup)

            print_page(i,nb_pages) # fonction d'affichage de l'avancement


            sleep(SLEEP_TIME)

    return soup_tab

#récupère les données détaillées de la fiche du tournoi. Non utilisé dans le mail
def scrap_details(url):
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, "html.parser")
     
    dict_details = {}

    table = soup.find_all("table")

    #une seule table dans les pages de details = table[0]
    rows = table[0].find_all('tr')
        
    for row in rows:
        cols = row.find_all('td')
        
        if cols[0].text == "Dates : ":
            dict_details["dates"] = unidecode.unidecode(cols[1].text)
            
        if cols[0].text == "Nombre de rondes : ":
            dict_details["nb_Rondes"] = cols[1].text

        if cols[0].text == "Cadence : ":
            dict_details["cadence"] = unidecode.unidecode(cols[1].text)
            
        if cols[0].text == "Adresse : ":
            dict_details["adresse"] = unidecode.unidecode(cols[1].text)
            
        if cols[0].text == "Annonce : ":
            dict_details["annonce"] = unidecode.unidecode(cols[1].text)
            
                
        
    return dict_details    



#récupère les données de chaque page récupérer par BS4 et les mets en forme dans un Dict compatible format JSON
def soup_to_dict(soup_tab, cadence, nb_pages):

    tournaments_tab = []

    for soup in soup_tab:

        table = soup.findAll("table")

        #table des tournois commence à l'index [2], ou [1] si une seule page car pas de liens vers les autres pages
        if nb_pages == 0:
            rows = table[1].find_all('tr')
        else:
            rows = table[2].find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')

            tournament_tab =[]

            for element in cols:
                tournament_tab.append(element.text)

            tournaments_tab.append(tournament_tab)

    #reformate tournoi
    tournaments_dicts = []

    for tournament in tournaments_tab:

        #pour les lignes titres des mois : mars 2023, avril 2023 => récupère l'année en cours pour la mettre dans le dict
        if len(tournament) < 2:
            fetched_annee = tournament[0].split(" ")[1]
        
        
        if len(tournament) > 1:
            
            #trouve le jour et le mois du tournois
            split_date = tournament[4].split(" ")
            
            dict = {"num_tournoi": tournament[0],
                    "cadence": cadence.name, 
                    "ville": tournament[1],
                    "dept": tournament[2],
                    "nom_tournoi": unidecode.unidecode(tournament[3]), # pour enlever les accents non reconnu en json  
                    "date": unidecode.unidecode(tournament[4]), # pour enlever les accents non reconnu en json     
                    "jour": reformate_jour(split_date[0]),
                    "mois": MONTH.get(split_date[1]),
                    "annee": fetched_annee,
                    "url_details": "http://www.echecs.asso.fr/FicheTournoi.aspx?Ref=" + tournament[0],
                    "details_tournoi": scrap_details("http://www.echecs.asso.fr/FicheTournoi.aspx?Ref=" + tournament[0])    
                    }            
            tournaments_dicts.append(dict)
        
    return tournaments_dicts




# ajoute un 0 devant si jour 1 chiffre seulement
def reformate_jour(jour):
    if len(jour) == 1:
        jour = "0" + jour

    return jour

# crée la structure du dict compatible pour transformation en JSON
def create_json_structure(full_dicts_tournois):
    dict_json = { 
        "date_maj": str(datetime.date.today()),
        "tournois": full_dicts_tournois,
    }    
    return dict_json
   


#enregistre les données dans un JSON
def write_database_json(data, name_file):

    with open(name_file, "w") as outfile:
        json.dump(data, outfile, indent=2)