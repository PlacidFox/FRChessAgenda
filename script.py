import os
from cli_display.cli_display import end_script, intro_text, state_DB
from functions.mail_structure import prepare_data_first_mail, prepare_data_mail

from functions.scrap_data import init_fetch_data, maj_fetch_data

from functions.values import jsonFiles
from functions.mail_send import send_mail


# affichage du texte d'introduction du script + de l'état de la base
intro_text()
state_DB()


# selon si base existant ou non : initialisation ou MAJ
if os.path.exists(jsonFiles.FULL_JSON.value):
    maj_fetch_data()
    end_script()
    send_mail(prepare_data_mail())
    
else:
    init_fetch_data()
    end_script()
    send_mail(prepare_data_first_mail())




