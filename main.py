from extract_data import user_ids, get_user
from transform_data import generate_ai_news
from load_data import upload_news

users_data = [user for id in user_ids if (user := get_user(id)) is not None]

for user in users_data:
    news = generate_ai_news(user)
    upload_news(user, news)


