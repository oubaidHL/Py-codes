import os
import re
import sys


def error_search(log_file):
    # demander à l’utilisateur de saisir l’erreur
    error = input("donner votre erreur? ")
    error_patterns = ["error"]
    # Construire le motif error_patterns (liste) à partir de error
    # error_patterns liste formé par les mot de error mais en minuscule
    for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
    # ajouter les lignes du fichier de log qui correspondent au motif à la liste
    # returned_errors
    # enfin, renvoyer returned_errors
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
    file.close()
    return returned_errors


def file_output(returned_errors):
    with open(os.getcwd+ '../data/errors_found.log','w') as file:  
        # os.path.expanduser('~') vai retornar o homepath
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    # à log_file on affecte le paramètre en ligne du script (le chemin du fichier contenant les log)
    log_file = sys.argv[1]
    returned_errors = error_search('/data/fishy.log')
    file_output(returned_errors)
    sys.exit(0)
