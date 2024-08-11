import sys
import os

# Ajoute le répertoire actuel au sys.path pour que Python puisse trouver app_api_flask
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app_api_flask import app

def test_homepage():
    client = app.test_client()  # Crée un client de test
    response = client.get('/')  # Simule une requête GET à la route '/'
    assert response.status_code == 200  # Vérifie que la réponse est 200 (OK)
