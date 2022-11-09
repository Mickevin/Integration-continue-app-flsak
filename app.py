from flask import Flask, render_template, request
import requests
import warnings
import time

# Données à afficher
#Adresses IP de la semabox / Nom de la semabox
#o IP publique de l’accès Internet / nom dns dynamique
#o Etat de la connexion Internet
#o Liste des machines détectées sur le réseau
#o Résultats du dernier test de débit

warnings.filterwarnings('ignore')

def date_time():
    day = time.localtime().tm_mday
    month = time.localtime().tm_mon
    year = time.localtime().tm_year
    
    return f'{day}/{month}/{year}'

date = date_time()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def app_home():
    return render_template("index.html", date=date)


@app.route('/submit/', methods=['POST'])
def result():    
    if request.method == 'POST':
        return render_template("submit.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=4000,)