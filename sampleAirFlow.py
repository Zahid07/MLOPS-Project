from airflow import DAG
from airflow.operators.python import PythonOperator 
from datetime import datetime

def print_hello():
    print('hello world')
    return 'Hello world!'

with DAG('hello_world_dag',
            start_date=datetime(2021, 1, 1),
            schedule='@daily',
            catchup=False) as dag:
    
        opr_hello = PythonOperator(task_id='say_Hi',
                                python_callable=print_hello)
        
opr_hello

