import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ouverture du fichier .ini pour récupérer les paramètres 
import configparser
config = configparser.ConfigParser()
config.read('parametersfiles/config.ini')

# Import des informations : Sender parameters
smtp_address = config["Mail_Sender"]["smtp_address"]
smtp_port = config["Mail_Sender"]["smtp_port"]
email_address = config["Mail_Sender"]["sender_email"]
email_password = config["Mail_Sender"]["sender_api_key"]

# EImport des informations : Mail Receiver (split par ; pour formattage en list)
email_receiver = config["Mail_Receiver"]["receiver"]
list_receivers_mail = email_receiver.split(";")


# on crée un e-mail
message = MIMEMultipart("alternative")
# on ajoute un sujet
message["Subject"] = "[Tournois Echec] mise à jour de la DB"
# un émetteur
message["From"] = "[Update Chess Tournois]" 
# un/des destinataire(s)
message["To"] = ", ".join(list_receivers_mail)


#envoie l'email avec les datas fournies en arguments (initialisation ou MAJ)
def send_mail(html_data):
    #conversion du code HTML du contenu du mail en MIME Text
    html_mime = MIMEText(html_data, 'html')

    # on attache cet élément 
    message.attach(html_mime)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_address, email_password)
        # envoi du mail
        server.sendmail(email_address, list_receivers_mail, message.as_string())


