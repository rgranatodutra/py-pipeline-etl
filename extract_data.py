import pandas
import requests
from global_vars import sdw2023_api_url

data_frame = pandas.read_csv("SDW2023.test.csv")
user_ids = data_frame["UserID"].tolist()

def get_user(id):
    get_url = f"{sdw2023_api_url}/users/{id}"
    response = requests.get(get_url)

    if response.status_code == 200:
        user = response.json()
        print(f"Sucessfully loaded user \"{user['name']}\". id = {id}")
        return user

    return None

