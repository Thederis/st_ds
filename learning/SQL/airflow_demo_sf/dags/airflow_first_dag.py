import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG("airflow_first_dag",
         start_date=pendulum.datetime(2023, 7, 10, tz=pendulum.timezone("Europe/Moscow")),
         schedule="@daily", catchup=False
) as dag:
    task = EmptyOperator(task_id="task")
