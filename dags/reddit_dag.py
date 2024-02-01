from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'YJ Zhu',
    'start_date': datetime(2024, 1, 29),
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup= False,
    tags=['reddit', 'etl', 'pipeline'],
)

# extract from reddit
extract = PythonOperator(
    task_id='reddit_extract',
    python_callable=reddit_pipeline,
    op_kwargs={
        'filename': f"reddit_{file_postfix}",
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },



# upload to s3