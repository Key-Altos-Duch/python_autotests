import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '29cf3e7d3435c6a8687abea858427215'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
body_create_pokemon = {
    "name": "оксич",
    "photo_id": 10
}
body_name_change = {
    "pokemon_id": "307108",
    "name": "токсич",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "307108"
}
response = requests.post(url = f'{URL}pokemons', headers = HEADER, json = body_create_pokemon)
print(response.text)

response_name_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_name_change)
print(response_name_change.text)

response_add_pokeball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response.json['message']
print(message)