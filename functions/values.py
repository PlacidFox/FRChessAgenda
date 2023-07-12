from enum import Enum


# Liste des cadences avec l'url de la page des tournois  
class CADENCES(Enum): 
       Longue = "http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=1"
       #HKO = "http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=2"
       Rapide = "http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=3"
       Blitz = "http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=4"



# Liste des fichiers de data format JSON avec leur emplacement
class jsonFiles(Enum): 
       FULL_JSON = "./db/db.json" 
       OLD_FULL_JSON = "./db/old_db.json"


# Pause entre chaque page. Nécessaire pour récupération des informations avant passage à la page suivante et éviter un bug avec des informations incomplètes si chargement long de la page web
SLEEP_TIME = 1.5


# Dict pour mapping des noms des mois affichés sur le site de la FFE. 
# Non utilisé dans le mail mais stocké dans le fichier JSON. Utilisable pour recherche sur une date ou un mois donné
MONTH ={"janv.": "01",
       "févr.": "02",
       "mars": "03",
       "avr.": "04",
       "mai": "05",
       "juin": "06",
       "juil.": "07",
       "août": "08",
       "sept.": "09",
       "oct.": "10",
       "nov.": "11",
       "déc.": "12"
}


# structure HTML pour construction message
HTML_START = '''
<html>
<body>
 '''

HTML_CHAPTER_NEW = '''
<p>     </p>
<h1>Liste des Nouveaux Tournois d'Echec</h1>
<p>     </p>
'''

HTML_CHAPTER_NEW_LONGUES = '''
<h3>New Parties Longues</h3>
<ul>
'''
       
HTML_CHAPTER_NEW_RAPIDES = '''
</ul>
<p>     </p>
<h3>New Parties Rapides</h3>
<ul>
'''
    
HTML_CHAPTER_NEW_BLITZ = '''
</ul>
<p>     </p>
<h3>New Parties Blitz</h3>
<ul>
'''

HTML_CHAPTER_ALL = '''
</ul>
<p>     </p>
<p>     </p>
<h1>Liste des Tournois d'Echec des Départements proches</h1>
<p>     </p>
'''

HTML_CHAPTER_ALL_LONGUES = '''
<h3>Parties Longues</h3>
<ul>
'''
       
HTML_CHAPTER_ALL_RAPIDES = '''
</ul>
<p>     </p>
<h3>Parties Rapides</h3>
<ul>
'''
    
HTML_CHAPTER_ALL_BLITZ = '''
</ul>
<p>     </p>
<h3>Parties Blitz</h3>
<ul>
'''

HTML_END = '''
</ul> 
</body>
</html>
'''