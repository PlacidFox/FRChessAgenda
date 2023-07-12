# FRChessAgenda

Script Python permettant de récupérer la liste des tournois d'échecs affichés sur le site de la Fédération Française des Echecs (FFE) : http://www.echecs.asso.fr/

Utilisation de Selenium pour récupérer les données des pages des tournois :
- Cadence Lente : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=1
- Cadence Rapide : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=3
- Cadence Blitz : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=4



Sauvegarde des données dans un fichier au format JSON (./db/db.json) :

Si db.json lors d'une nouvelle exécution du script:
- transformation du fichier db.json en old_db.json
- déroulé du script de web-scrapping
- mise en forme des nouvelles données dans un nouveau fichier db.json
- comparaison entre les deux fichiers en utilisant le paramètres unique : "num_tournoi" pour connaître les nouvelles annonces de tournois depuis la dernière execution du script


Puis envoi d'un email avec la liste des nouveaux tournois par cadence et mise en forme pour des listes de départements pré-définis + liste de tous les tournois existants dans le fichier db.jdon

#### besoin Python 3.10 minimum
#### 1H KO non mis en forme dans le mail a ajouter dans le fichier mail.py si souhaité
#### Tournois en cadence 1H Ko non activée dans le script mais possible en enlevant la mise en commentaires du paramètres HKO dans le fichier constantes.py dans le répertoire /constantes


### Resultat par mail

- Liste des nouveaux tournois depuis la dernière execution du script
puis
- Liste de tous les tournois affichés sur le site de la FFE

#### possible de définir si affichage uniquement des tournois de deux listes de département (dept_proche et dept_long) ou alors de tous les tournois de France


### Pre-requis

- Google Chrome ou Chromium installé
- Utilisation d'une adresse gmail pour l'envoi
- Création d'une API KEY Google : https://support.google.com/accounts/answer/185833?visit_id=638228855488727653-4017096174&p=InvalidSecondFactor&rd=1

#### A modifier dans le fichier /parametersfiles/config.ini :

- liste_dept_proche : (tournois de ces départements sont indiqués en rouge dans le mail reçu)
- liste_dept_long : (tournois de ces départements sont indiqués en gras dans le mail reçu)
- sender_email : adresse Gmail qui envoie l'email
- sender_api_key : API KEY nécessaire pour l'authentification au compte Gmail
- receiver : adresse mail qui reçoit le mail de synthèse

- [Display_Parameters] show_only_list
  -  si False : ne montre dans le mail qui les tournois des Dept Proche et Long.
  -  si True : montre tous les tournois de France
