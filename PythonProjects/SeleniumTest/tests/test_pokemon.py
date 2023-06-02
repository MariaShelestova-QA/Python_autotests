import pytest
import requests

host = 'https://pokemonbattle.me:9104'
token = '30a85ab22ea7194668e1690a8cdedab9'

def test_status_code():
    answer_status = requests.get(f'{host}/trainers',
                    headers = {"Content-Type": "application/json", "trainer_token": token})
    
    assert answer_status.status_code == 200


def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {"trainer_id": 4634})
    
    assert answer_body.json()['trainer_name'] == 'Мария'