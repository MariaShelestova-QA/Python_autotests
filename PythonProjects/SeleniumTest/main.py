import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '30a85ab22ea7194668e1690a8cdedab9'

answer = requests.post(f'{host}/pokemons', json = {
    "name": "Мими",
    "photo": "https://dolnikov.ru/pokemons/albums/039.png"
}, 
headers = {"Content-Type": "application/json", "trainer_token": token})

print(answer.text)


answer_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12714",
    "name": "Talig",
    "photo": "https://dolnikov.ru/pokemons/albums/039.png"
}, headers = {"Content-Type": "application/json", "trainer_token": token})

print(answer_name.text)



answer_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    
    "pokemon_id": "12714"

}, 
headers = {"Content-Type": "application/json", "trainer_token": token})

print(answer_pokeball.text)

