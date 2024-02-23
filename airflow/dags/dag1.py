import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
# from airflow.operators.bash_operator import BashOperator



# Now try importing the 'main' function from the respective Python files within the 'scripts' subdirectory
try:
    # from scripts.webscrape import main as webscrape_main
    from scripts.app import main as app_main
    from scripts.grobid import main as grobid_main
except ModuleNotFoundError as e:
    print(f"Error importing modules: {e}")
    raise

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),  # Adjust to your actual start date
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'python_operator_dag',
    default_args=default_args,
    description='A simple DAG with PythonOperator',
    schedule_interval=timedelta(days=1),  # Adjust the interval as needed
)

# install_requirements = BashOperator(
#     task_id='install_requirements',
#     bash_command=f'pip install -r {os.path.join(os.path.dirname(__file__), "scripts/requirements.txt")}',
#     dag=dag,
# )

# Define the tasks
# def webscrape_function():
#     webscrape_main()

def app_function():
    app_main()

def grobid_function():
    grobid_main()

# task1 = PythonOperator(
#     task_id='webscrape',
#     python_callable=webscrape_function,
#     dag=dag,
# )

task2 = PythonOperator(
    task_id='app',
    python_callable=app_function,
    dag=dag,
)

task3 = PythonOperator(
    task_id='grobid',
    python_callable=grobid_function,
    dag=dag,
)

# Set the task execution order
task2 >> task3