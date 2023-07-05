import pytest
import requests
import json
import time

# import sys
# sys.path.insert(0, './project/app/schemas')
# from project.app.schemas import AuthDetails

from ..app.schemas import AuthDetails

from decouple import config

def test_get_all_users():
    resp = requests.get(f'{config("api_url")}/users')
    # resp = requests.get('http://127.0.0.1:8000/users')
    assert resp.status_code == 200

#LOGGIN =================================================================================================
@pytest.mark.parametrize('auth_details, expected_result', [(AuthDetails(email='test@mail.ru',  password='1234'), 401),
                                                           (AuthDetails(email='Roma@mail.com', password='4444'), 401),
                                                           (AuthDetails(email='Roma@mail.com', password='1234'), 200)])
def test_login(auth_details, expected_result):

    resp = requests.post(f'{config("api_url")}/user/login', json={'email': auth_details.email, 
                                                                  'password': auth_details.password})
    assert resp.status_code == expected_result

#REGISTRATION =================================================================================================
@pytest.mark.parametrize('auth_details, expected_result', [(AuthDetails(email='Roma@mail.com',      password='444'), 400), 
                                                           (AuthDetails(email='RomaRomov@mail.com', password='444'), 201)])
def test_registration(auth_details, expected_result):
    resp = requests.post(f'{config("api_url")}/user/register', json={'auth':{'email': auth_details.email, 
                                                                            'password': auth_details.password}})
    
    assert resp.status_code == expected_result

#TOKEN =================================================================================================
@pytest.mark.parametrize('auth_details, expected_result', [(AuthDetails(email='Gio@mail.com', password='1234'), "Not authenticated"), 
                                                           (AuthDetails(email='Roma@mail.com', password='1234'), "Authenticated"), 
                                                           (AuthDetails(email='Alex@mail.com', password='4321'), "Signature has Expired")] )
def test_token(auth_details, expected_result):
    resp = requests.post(f'{config("api_url")}/user/login', json={'email': auth_details.email, 
                                                                  'password': auth_details.password})
    
    token = ''

    #если залогинились, то получим токен
    if resp.status_code == 200: 
        token = json.loads(resp.text)['detail']['token']

    headers = {"Authorization": f"Bearer {token}"}
    #проверим если время токена закончится для аккаунта с почтой Alex@mail.com сделаем паузу на время и отправим запрос
    if (auth_details.email == 'Alex@mail.com'):
            time.sleep(int(config("token_expired_seconds")) + 5)

    resp = requests.get(f'{config("api_url")}/protected', headers=headers)
    data = json.loads(resp.text)

    if resp.status_code != 200: assert data['detail'] == expected_result
    else:                       assert data['detail']['authenticated'] == expected_result

