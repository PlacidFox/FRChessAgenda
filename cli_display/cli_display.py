import os
import platform
from functions.read_data import open_json

from functions.values import jsonFiles

def intro_text():
    print("=== Script de récupération des annonces de tournois d'echec en France ===")
    empty_line()

def state_DB():
    if os.path.exists(jsonFiles.FULL_JSON.value):
        data = open_json(jsonFiles.FULL_JSON)
        date_maj = data["date_maj"]
        
        print(f"Mise à jour de la base... (Dernière MAJ : {date_maj})")
        empty_line()
    else:
        print("Base inexistante. Création de la base initiale ...")
        empty_line()


def launch_scrap(cadence):
    print(f"Démarrage de la récupération des tournois : {cadence}")

def print_page_find(nb_pages):
    print(f"Nb de pages à scroller : {nb_pages - 2}") # -2 pour enlever les liens trouvés pour les fleches
    empty_line()

def print_page(nbpage, totalpage):
    print(f"Page n° {nbpage} / {totalpage - 2 } faite") # -2 pour enlever les liens trouvés pour les fleches

def end_scrap(cadence):
    empty_line()
    print(f"Récupération des tournois : {cadence} terminées")
    print("Traitement des données... (veuillez patienter)")
    empty_line()

def end_script():
    clear_screen()
    print("Récupération des tournois terminée. Envoi de l'email en cours...")

def empty_line():
    print("")


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Linux":
        os.system("clear")

