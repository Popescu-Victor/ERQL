from google.cloud import bigquery
import pandas as pd
import json



def json_to_bigquery(json_file_path, project_id, dataset_id, table_id):

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    df = pd.json_normalize(data)
    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"


    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True
    )
    
    load_job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    
    load_job.result() 

    print(f"Data loaded to {table_ref} successfully.")