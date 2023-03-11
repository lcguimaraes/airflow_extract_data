import requests
import pandas as pd
import json
from time import sleep

API_KEY_NEWS = "1bc686c14173333004b94d414099c136"
word_search = "trends"

url = f"https://gnews.io/api/v4/search?q={word_search}&apikey={API_KEY_NEWS}"

response = requests.get(url)
sleep(60)

if response.status_code >= 200 and response.status_code <= 299:
    news_data = response.json()

    news_dict = {
        "title": [],
        "name": [],
        "url": []
    }

    for new in news_data["articles"]:
        news_dict["title"].append(new["title"])
        news_dict["name"].append(new["source"]["name"])
        news_dict["url"].append(new["source"]["url"])
    
    df_news = pd.DataFrame(news_dict)

    df_news.to_parquet("~/airflow/scripts/database_news_temp/news.parquet")
else:
    raise Exception(f"The response for the request is {response.status_code}")