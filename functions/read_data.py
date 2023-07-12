import json

from functions.values import jsonFiles


# ouvre un ficher db.json pour lecture des données
def open_json(JSON):

    with open(JSON.value, "r") as jsonFile:
        return json.load(jsonFile)



#recup une liste des nouveaux tournois dans la base JSON qui n'existe pas dans la base précédente. Comparaison avec 
def get_list_tournois_new():

    new_data = open_json(jsonFiles.FULL_JSON)
    old_data = open_json(jsonFiles.OLD_FULL_JSON)

    list_tournaments_old = []
    list_tournaments_new = []

    for tournament in old_data["tournois"]:
        list_tournaments_old.append(tournament["num_tournoi"])

    #crée une liste des nouveaux tournois pas existants dans la base
    for tournament in new_data["tournois"]:
        if tournament["num_tournoi"] not in list_tournaments_old:
            list_tournaments_new.append(tournament)

    return list_tournaments_new


#retourne une liste de tous les tournois existants dans la base JSON
def get_list_tournois():
    
    data = open_json(jsonFiles.FULL_JSON)
    list_tournaments = []

    for element in data["tournois"]:
        list_tournaments.append(element)

    return list_tournaments
