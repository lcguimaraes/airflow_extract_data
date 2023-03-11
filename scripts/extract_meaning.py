import pandas as pd
import pyarrow as pa
import datetime as dt
import pyarrow.parquet as pq
import requests
from os import path
from time import sleep

API_KEY_MEANING = ""

df_news = pd.read_parquet("~/airflow/scripts/database_news_temp/news.parquet")

SCORE_TAGS_MEANING = {
    "P+":     "P+: strong positive",
    "P":      "P: positive",
    "NEU":    "NEU: neutral",
    "N":      "N: negative",
    "N+":     "N+: strong negative",
    "NONE":   "NONE: without polarity"
}

meaning_dict = {
    "score_tag": []
}

for title in df_news["title"]:
    files = {
        'key': (None, API_KEY_MEANING),
        'lang': (None, 'en'),
        'txt': (None, title),
    }

    response = requests.post('https://api.meaningcloud.com/sentiment-2.1', files=files)
    sleep(5)
    
    if response.status_code >= 200 and response.status_code < 299:
        meaning = response.json()
        data_score_tag = SCORE_TAGS_MEANING[ meaning["score_tag"] ]
        
        meaning_dict["score_tag"].append(data_score_tag)
    else:
        meaning_dict["score_tag"].append("Bad Request")

df_meaning = pd.DataFrame(meaning_dict)

df_data = pd.concat([df_news, df_meaning], axis=1)

today = dt.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

if path.exists(f"~/airflow/scripts/database/news_{today}.parquet"):
    database_news = pd.read_parquet(f"~/airflow/scripts/database/news_{today}.parquet")

    new_database = pd.concat([database_news, df_data], axis=0, ignore_index=True)

    new_database.to_parquet(f"~/airflow/scripts/database/news_{today}.parquet")
else:
    df_data.to_parquet(f"~/airflow/scripts/database/news_{today}.parquet")