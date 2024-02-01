pip install apache-airflow pandas numpy praw

mkdir config dags data etls logs pipelines tests utils

touch airflow.env docker-compose.yml Dockerfile

pip freeze > requirements.txt

finish airflow.env, docker-compose.yml, Dockerfile

docker compose up -d --build

write dags/reddit_dag.py
