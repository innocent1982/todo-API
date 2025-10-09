import requests
from getpass import getpass

username = input("username: ")
password = getpass("password: ")
email = input("email: ")
age = int(input("age: "))
phone = input("Phone (+265 / 0): ")
user_data = {
    'username':"pempho",
    'password':"inno2006",
    'email':"innocent@gmail.com",
    'age':19,
    'phone':"0991644084",
    "is_staff":True
}


def create_user():
    endpoint = "http://127.0.0.1:8000/api/user/"
    response = requests.post(endpoint, json=user_data)
    if response.status_code == 200:
        print("Success")
    else:
        print(response.text)

create_user()

