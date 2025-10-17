import requests
from user import create_user, get_credentials 
from datetime import datetime

credentials = get_credentials()

def create_task():
    endpoint = "http://127.0.0.1:8000/api/task/create/"
    task = {
        "name": input("Enter name :"),
        "description": input("Description: "),
        "start_time": str(datetime.now()),
        "end_time": str(datetime(2025, 11, 5, 12, 00))
    }
    headers = {
        "content-type":"application/json",
        "Authorization": f"Bearer {credentials["access"]}"
    }
    response = requests.post(endpoint, json=task, headers=headers)
    if response.status_code == 200:
        print("Success")
    return response.json()

def get_task():
    endpoint = "http://127.0.0.1:8000/api/task/get/"
    headers = {
        "content-type":"application/json",
        "Authorization": f"Bearer {credentials["access"]}"
    }
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        print("Success")
    return response.json()


print(get_task())
    

