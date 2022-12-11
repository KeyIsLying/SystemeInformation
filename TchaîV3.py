## Systèmes d'Information Avancés
#  Projet TP

# Tchaî V3

from flask import *
import csv
import os
import hashlib
from datetime import datetime

app = Flask(__name__)

transaction = []
fichier = "D:/Clément GRENOT/Documents/ESIREM/5A/Système d'information avancé/transactionV3.csv"


# Ajout de quelque transactions pour simplifier durant les tests
# transaction = [["clement","hugo","50"],["arthur","hugo","5"],["arthur","clement","15"],["hugo","kilian","31"]]

## Page d'accueil
@app.route('/')
def home():
    list_ = []
    integrity = True
    # Lecture fichier de sauvegarde
    transaction.clear()
    if os.path.exists(fichier) == False:
        creation = open(fichier, 'w')
        creation.close()
    with open(fichier) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            transaction.append(row)
    for i in range(len(transaction)):
        if transaction[i]:
            list_.append(
                transaction[i][0] + '  ' + transaction[i][1] + '  ' + transaction[i][2] + ' ' + transaction[i][3])
            # Récupération hash précédent
            if i == 0:
                previousHash = '0'
            else:
                previousHash = transaction[i - 1][4]
            print(previousHash)
            tuple_ = (transaction[i][0], transaction[i][1], transaction[i][2], transaction[i][3], previousHash)
            integrity = check_integrity(transaction[i][4], tuple_)
    if integrity:
        result = 'Integrité valide'
    else:
        result = 'Integrité non valide'

    return 'Tchaî V3 <ul>' + str(result) + ''.join(
        ['<li> ' + i for i in list_]
    ) + '<ul>\n', 200


## Création d'une nouvelle transaction
@app.route('/new_Transac/<emetteur>/<recepteur>/<montant>', methods=['GET'])
def NewTransaction(emetteur, recepteur, montant):
    # transaction.append([emetteur,recepteur,montant])
    transaction.clear()
    if os.path.exists(fichier) == False:
        creation = open(fichier, 'w')
        creation.close()
    with open(fichier) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            transaction.append(row)
    ## Ecriture dans le fichier csv
    # Récupération date
    date_now = datetime.now()
    dt_string = date_now.strftime("%d-%m-%Y %H:%M:%S")
    # Récupération hash précédent
    if len(transaction)==0:
        previousHash = '0'
    else:
        previousHash = transaction[len(transaction)-1][4]
    # Calcul hash
    tuple_ = (emetteur, recepteur, montant, dt_string, previousHash)
    hashed = calculHash(tuple_)


    with open(fichier, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow([emetteur, recepteur, montant, dt_string, hashed, previousHash])
    return 'Nouvelle transaction entre ' + emetteur + ' et ' + recepteur + ' de ' + montant + ' le ' + dt_string + ' .\n', 200
    # Création d'une nouvelle transaction : curl -X GET localhost:5000/new_Transac/clement/hugo/50


## Page historique pour un user
@app.route('/historique/<utilisateur>', methods=['GET'])
def Historique(utilisateur):
    list_ = []
    # Lecture fichier de sauvegarde
    transaction.clear()
    if os.path.exists(fichier) == False:
        creation = open(fichier, 'w')
        creation.close()
    with open(fichier) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            transaction.append(row)

    for i in range(len(transaction)):
        if (utilisateur in transaction[i][0]) or (utilisateur in transaction[i][1]):
            list_.append(
                transaction[i][0] + '  ' + transaction[i][1] + '  ' + transaction[i][2] + ' ' + transaction[i][3])

    return 'Tchaî V3 - Historique de ' + utilisateur + '  <ul>' + ''.join(
        ['<li> ' + i for i in list_]
    ) + '<ul>\n', 200
    # Historique : culr -X GET localhost:5000/historique/clement


## Calcul du solde d'un utilisateur
@app.route('/solde/<utilisateur>', methods=['GET'])
def Solde(utilisateur):
    solde = 0

    # Lecture fichier de sauvegarde
    transaction.clear()
    if os.path.exists(fichier) == False:
        creation = open(fichier, 'w')
        creation.close()
    with open(fichier) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            transaction.append(row)

    for i in range(len(transaction)):
        if (utilisateur in transaction[i][0]):
            solde -= int(transaction[i][2])

        if (utilisateur in transaction[i][1]):
            solde += int(transaction[i][2])
    return 'solde ' + str(solde) + ' \n', 200
    # Solde : curl -X GET localhost:5000/solde/clement


def convertTuple(tuple_):
    string_ = ''
    for i in tuple_:
        string_ = string_ + i
    return string_


def calculHash(tuple_):
    string_ = convertTuple(tuple_)
    string_ = string_.encode("utf-8")
    hash_ = hashlib.sha256(string_).hexdigest()
    return hash_


def check_integrity(hash_, tuple_):
    test = calculHash(tuple_)
    if hash_ == test:
        return True
    else:
        return False


app.run(host='0.0.0.0', debug=True)
