from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

with DAG(
	"news_collector",
	default_args = {
		"depends_on_past": False,
		"email": ["email@gmail.com" ],
		"email_on_failure": False,
		"email_on_retry": False,
		"retries": 2,
		"retry_delay": timedelta( minutes = 10 )
	},
	description = "News collector",
	schedule_interval = "*/10 * * * *",
	start_date = datetime(2021,1,1),
	end_date = datetime(2025,1,1),
	catchup = False,
	tags = ["collector", "news"],
) as dag:
	task1 = BashOperator(
		task_id = "extract_news",
		bash_command = "python3 ~/airflow/scripts/extract_news.py",
	)
	task2 = BashOperator(
		task_id = "extract_meaning",
		bash_command = "python3 ~/airflow/scripts/extract_meaning.py",
	)
	task3 = BashOperator(
		task_id = "remove_files",
		bash_command = "rm ~/airflow/scripts/database_news_temp/news.parquet",
	)
	task1 >> task2 >> task3
