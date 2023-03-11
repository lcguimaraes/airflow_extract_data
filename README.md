# Final data extraction project

## About the project

The goal of this project is to practice basic concepts of Airflow 

This project uses the two public APIs [Gnews](https://gnews.io/) and [Sentiment Analysis](https://www.meaningcloud.com/products/sentiment-analysis)

In this project a DAG is created with three tasks, one for extracting news, another for extracting the sentiment of the news and the third cleans the folders with temporary files


- Task 1: Extracts 10 trends news and saves it in a .parquet file in the database_news_temp folder
- Task 2: It reads the .parquet with the 10 temporary news items and extracts the news sentiment for each news item. Saving the information data of the 10 news along with the sentiment in a .parquet file in the database folder.
- Task 3: Remove the temporary .parquet file from the database_news_temp folder

## Install airflow and other python dependencies

Create the virtual environment and install the dependencies through the requirements.txt file

```bash
    python3 -m venv airflow_env  # Create virtual env
    source airflow_env/bin/activate # Activate the virtual environment
    pip install -r requirements.txt # Install all dependencies in the virtual environment
```

## Settings

Don't forget to put the API_KEYS value

- API_KEY_MEANING : scripts/extract_meaning.py
- API_KEY_NEWS : scripts/extract_news.py