import datetime

from airflow import models
from airflow.providers.google.cloud.operators.dataflow import DataflowCreatePythonJobOperator
from airflow.utils.dates import days_ago

bucket_path = "gs://<bucket name>"
project_id = "<project name>"
gce_zone = "us-central1-a"
import pytz

tz = pytz.timezone('US/Pacific')
tstmp = datetime.datetime.now(tz).strftime('%Y%m%d%H%M%S')

default_args = {
    # Tell airflow to start one day ago, so that it runs as soon as you upload it
    "start_date": days_ago(1),
    "dataflow_default_options": {
        "project": project_id,
        # Set to your zone
        "zone": gce_zone,
        # This is a subfolder for storing temporary files, like the staged pipeline job.
        "tempLocation": bucket_path + "/tmp/",
    },
}


with models.DAG(
    "composer_dataflow_dag",
    default_args=default_args,
    schedule_interval=datetime.timedelta(days=1),  # Override to match your needs
) as dag:

    create_mastertable = DataflowCreatePythonJobOperator(
        task_id="create_mastertable",
        py_file=f'gs://<bucket name>/dataflow-job.py',
        options={"runner":"DataflowRunner","project":project_id,"region":"us-central1" ,"temp_location":"gs://<bucket name>/", "staging_location":"gs://<bucket name>/"},
        job_name=f'job{tstmp}',
        location='us-central1',
        wait_until_finished=True,
    )
