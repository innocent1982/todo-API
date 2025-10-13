import requests
from getpass import getpass
import json

def verify_token(token):
    endpoint = "http://127.0.0.1:8000/api/auth/token/verify/"
    data = {
        "token": token 
    }
    response = requests.post(endpoint, json=data)
    if response.status_code == 200:
        return "OK"
    return "INVALID"

def get_tokens():
    username = input("Username: ")
    password = getpass("password: ")
    data = {
        "username":username,
        "password":password
    }
    endpoint = "http://127.0.0.1:8000/api/auth/token/"
    response = requests.post(endpoint, json=data)
    if response.status_code == 200:
        credentials = response.json()
        with open("storage.json", "w") as f:
            json.dump(response.json(), f)
        return response.json()
    print("Authenticatipn failed")
    print(response.status_code)
    print(response.json())


credentials = None
if credentials == None:
    with open("storage.json", "r") as f:
        data = json.load(f)
        if data:
            response = verify_token(data['access'])
            if response == "OK":
                credentials = data 
            else:
                print("Tokens Expired, Verify\n")
                new_data = get_tokens()
                credentials = new_data


def create_user():
    username = input("username: ")
    password = getpass("password: ")
    email = input("email: ")
    age = int(input("age: "))
    phone = input("Phone (+265 / 0): ")
    user_data = {
        'username':username,
        'password':password,
        'email':email,
        'age':age,
        'phone':phone,
    }
    endpoint = "http://127.0.0.1:8000/api/user/"
    response = requests.post(endpoint, json=user_data)
    if response.status_code == 200:
        print("Success")
    else:
        print(response.text)


def get_details():
    headers = {
        "Authorization": f"Bearer {credentials['access']}",
            "content-type":"application/json"
    }
    endpoint = "http://127.0.0.1:8000/api/user/details/"
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        print("Retreival successful")
        return response.json()
    print("Failed to retrieve details")


def modify_user():
    field = input("Field: ")
    value = input("Value: ")
    boolean_fields = ['is_superuser', 'is_staff', 'is_active']
    if field in boolean_fields:
        value = bool(value)
    data = {
        str(field):value
    }
    headers = {
        "Authorization": f"Bearer {credentials['access']}",
            "content-type":"application/json"
    }
    print(f"{field} - {value}")
    endpoint = "http://127.0.0.1:8000/api/user/modify/"
    response = requests.patch(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        print("User modified")
        return response.json()
    print("Failed to modify user")
    print(response.json())

create_user()
