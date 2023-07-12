# ouverture du fichier .ini pour récupérer les paramètres 
import configparser

from functions.read_data import get_list_tournois, get_list_tournois_new
from functions.values import CADENCES, HTML_CHAPTER_ALL, HTML_CHAPTER_ALL_BLITZ, HTML_CHAPTER_ALL_LONGUES, HTML_CHAPTER_ALL_RAPIDES, HTML_CHAPTER_NEW, HTML_CHAPTER_NEW_BLITZ, HTML_CHAPTER_NEW_LONGUES, HTML_CHAPTER_NEW_RAPIDES, HTML_END, HTML_START
config = configparser.ConfigParser()
config.read('parametersfiles/config.ini')

# import des listes de départements - vue comme de string pas des listes mais fonctionne
LIST_CLOSE_DEPT = config["Departement"]["liste_dept_proche"]
LIST_LONG_DEPT = LIST_CLOSE_DEPT + config["Departement"]["liste_dept_long"]

# import parametres affichage
if config["Display_Parameters"]["show_only_list"] == "True":
    show_all_tournaments = True
else:
    show_all_tournaments = False


def prepare_data_mail():

    tournaments_list = get_list_tournois()
    new_tournaments_list = get_list_tournois_new()

    #récupère la structure de chaque partie du fichier values.py
    html_chapter_new_longues = HTML_CHAPTER_NEW_LONGUES
    html_chapter_new_rapides = HTML_CHAPTER_NEW_RAPIDES
    html_chapter_new_blitz = HTML_CHAPTER_NEW_BLITZ

    html_chapter_all_longues = HTML_CHAPTER_ALL_LONGUES
    html_chapter_all_rapides  = HTML_CHAPTER_ALL_RAPIDES
    html_chapter_all_blitz = HTML_CHAPTER_ALL_BLITZ
    

    
    for tournoi in new_tournaments_list:
        list = ""
        
        match tournoi['cadence']:
            case CADENCES.Longue.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :   
                    if show_all_tournaments:
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_new_longues = html_chapter_new_longues + list
            case CADENCES.Rapide.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :     
                    if show_all_tournaments:           
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_new_rapides = html_chapter_new_rapides + list
            case CADENCES.Blitz.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :   
                    if show_all_tournaments:             
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_new_blitz = html_chapter_new_blitz + list
             
           
                
  
  
    for tournoi in tournaments_list:
        list = ""
        match tournoi['cadence']:
            case CADENCES.Longue.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :    
                    if show_all_tournaments:            
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_all_longues = html_chapter_all_longues + list
            case CADENCES.Rapide.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :    
                    if show_all_tournaments:            
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_all_rapides = html_chapter_all_rapides + list
            case CADENCES.Blitz.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :                
                    if show_all_tournaments:
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " +"</li>"
                html_chapter_all_blitz = html_chapter_all_blitz + list
                
                
        
    return (HTML_START + HTML_CHAPTER_NEW + html_chapter_new_longues + html_chapter_new_rapides + html_chapter_new_blitz + HTML_CHAPTER_ALL + html_chapter_all_longues + html_chapter_all_rapides + html_chapter_all_blitz + HTML_END)
    

def prepare_data_first_mail():

    tournaments_list = get_list_tournois()
    
    #récupère la structure de chaque partie du fichier values.py
    html_chapter_all_longues = HTML_CHAPTER_ALL_LONGUES
    html_chapter_all_rapides  = HTML_CHAPTER_ALL_RAPIDES
    html_chapter_all_blitz = HTML_CHAPTER_ALL_BLITZ

  
    for tournoi in tournaments_list:
        list = ""
        match tournoi['cadence']:
            case CADENCES.Longue.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :    
                    if show_all_tournaments:            
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_all_longues = html_chapter_all_longues + list
            case CADENCES.Rapide.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :    
                    if show_all_tournaments:            
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</li>"
                html_chapter_all_rapides = html_chapter_all_rapides + list
            case CADENCES.Blitz.name:
                if (tournoi['dept'] in LIST_LONG_DEPT):
                    list = "<li><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"
                    if (tournoi['dept'] in LIST_CLOSE_DEPT):
                        list = "<li style=\"color:#FF0000\";><b>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " + "</b></li>"                    
                else :                
                    if show_all_tournaments:
                        list = "<li>" + tournoi["date"] + " - " + tournoi["num_tournoi"] + " - " + tournoi["ville"] + " - " + tournoi['dept'] + " - " + tournoi["nom_tournoi"] + " - <a href=" + tournoi["url_details"] + ">Lien Fiche FFE</a> " +"</li>"
                html_chapter_all_blitz = html_chapter_all_blitz + list
                
                
        
    return (HTML_START + HTML_CHAPTER_ALL + html_chapter_all_longues + html_chapter_all_rapides + html_chapter_all_blitz + HTML_END)
    
