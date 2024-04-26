from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from pendulum import datetime, duration 
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.models.param import Param
from airflow.operators.bash_operator import BashOperator

default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": duration(minutes=1),
}

@dag(
    start_date=datetime(2024, 1, 1), schedule=None, default_args=default_args, params={ "run_date": Param("2024-03-30", type="string") }
)
def copy_committee_types_table():
    @task
    def begin():
        EmptyOperator(task_id="begin")

    @task
    def truncate_table():
        truncate_committee_types = """
        USE ELECTION.RAW;

        TRUNCATE TABLE election.raw.RAW_COMMITTEE_TYPES;
        """
        snowflake_query = SnowflakeOperator(
            task_id="snowflake_query",
            sql=truncate_committee_types,
            snowflake_conn_id="snowflake_conn"
        )
        snowflake_query.execute(context={})

    @task
    def copy_table(params):
        run_date = params["run_date"]
        copy_committee_types = f"""
        USE ELECTION.PUBLIC;

        COPY INTO election.raw.RAW_COMMITTEE_TYPES
        FROM @COMMITTEE_TYPES_STAGE/{run_date}_committee_types.csv
        ON_ERROR = 'SKIP_FILE_5%'
        FILE_FORMAT = FEC_CSV;
        """
        snowflake_query = SnowflakeOperator(
            task_id="snowflake_query",
            sql=copy_committee_types,
            snowflake_conn_id="snowflake_conn"
        )
        snowflake_query.execute(context={})
    
    @task
    def end():
        EmptyOperator(task_id="end")

    begin() >> truncate_table() >> copy_table() >> end()
copy_committee_types_table()