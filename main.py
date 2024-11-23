from fastapi import FastAPI
from google.cloud import bigquery
import os



app = FastAPI()


@app.post("/data_dump")
def gcs_csv2bq_table():
    big_query_client = bigquery.Client()

    gcs_csv_location='gs://gcpmlopsend2end/reviews_all_App.csv'
    bq_table='clv-03091991-vertexai.gcpmlops.reviews_all_app'
    job_config=bigquery.LoadJobConfig(write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE, 
                                        source_format=bigquery.SourceFormat.CSV,
                                        skip_leading_rows=1
                                        )
    
    load_job=big_query_client.load_table_from_uri(gcs_csv_location,
                                                  bq_table,
                                                  job_config=job_config)
    
    load_job.result()

    destination_table=big_query_client.get_table(bq_table)

    return {"data": destination_table.num_rows}

    







