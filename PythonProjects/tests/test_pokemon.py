import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '29cf3e7d3435c6a8687abea858427215'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '28124'

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '28124'

     