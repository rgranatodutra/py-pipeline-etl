import requests
from global_vars import sdw2023_api_url, sdw2023_credit_icon_url

def upload_news(user, news):
    put_url = f"{sdw2023_api_url}/users/{user['id']}"

    formated_news = {
        "icon": sdw2023_credit_icon_url,
        "description": news
    }

    user_with_news = user.copy()

    if user_with_news["news"]:
        user_with_news["news"].append(formated_news)
    else:
        user_with_news["news"] = [formated_news]

    response = requests.put(put_url, json=user_with_news)

    if response.status_code == 200:
        print(f"{user['name']} has received the news with success!")
    else:
        print(f"Failed to upload news for {user['name']}. status={response.status_code}")