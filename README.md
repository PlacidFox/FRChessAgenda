# FRChessAgendaAPI

Script Python permettant de récupérer la liste des tournois d'échecs affichés sur le site de la Fédération Française des Echecs (FFE) : http://www.echecs.asso.fr/

Utilisation de Selenium pour récupérer les données des pages des tournois :
- Cadence Lente : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=1
- Cadence Rapide : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=3
- Cadence Blitz : http://www.echecs.asso.fr/ListeTournois.aspx?Action=ANNONCE&Level=4

#### Tournois en cadence 1H Ko non activée dans le script mais possible en enlevant la mise en commentaires du paramètres HKO dans le fichier constantes.py dans le répertoire constantes/ (A METTRE A JOUR)

Sauvegarde des données dans un fichier au format JSON (./db/db.json) :

Si db.json lors d'une nouvelle exécution du script:
- transformation du fichier db.json en old_db.json
- déroulé du script de web-scrapping
- mise en forme des nouvelles données dans un nouveau fichier db.json
- comparaison entre les deux fichiers en utilisant le paramètres unique : "num_tournoi" pour connaître les nouvelles annonces de tournois depuis la dernière execution du script


Puis envoi d'un email avec la liste des nouveaux tournois par cadence et mise en forme pour des listes de départements pré-définis + liste de tous les tournois existants dans le fichier db.jdon

#### (A FAIRE) Guide pour inscrire les mails de réception dans le fichier ini si list de plusieurs mails

#### Fonctionne avec envoi depuis une adresse gmail

#### besoin Python 3.10 minimum

#### 1H KO non mis en forme dans le mail a ajouter dans le fichier mail.py si souhaité


Attention au navigateur, selon version Linux Chrome ou Chromium ?

pour create API KEY Google : https://support.google.com/accounts/answer/185833?visit_id=638228855488727653-4017096174&p=InvalidSecondFactor&rd=1



## TODO

Google Chrome ou Chromium d'installé
Utilisation d'une adresse gmail
Création d'une API KEY Google : https://support.google.com/accounts/answer/185833?visit_id=638228855488727653-4017096174&p=InvalidSecondFactor&rd=1

A MODIFIER DANS FICHIER : /parametersfiles/config.ini :
- liste_dept_proche = ['51', '10', '08', '52', '55', '77', '02']
liste_dept_long = ['89', '21', '54', '57', '67', '93', '94', '80', '60', '59']
sender_email = v
sender_api_key = 

[Mail_Receiver]
receiver = 
Recevier multiple ?
