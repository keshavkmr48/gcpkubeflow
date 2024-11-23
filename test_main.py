from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from main import app  # Import your FastAPI app

client = TestClient(app)


@patch("main.bigquery.Client")  # Mock the BigQuery Client
def test_gcs_csv2bq_table(mock_bigquery_client):
    # Mock the BigQuery client and its methods
    mock_client_instance = MagicMock()
    mock_bigquery_client.return_value = mock_client_instance

    # Mock the load_table_from_uri method and its return value
    mock_load_job = MagicMock()
    mock_client_instance.load_table_from_uri.return_value = mock_load_job

    # Simulate load_job.result() to complete without exceptions
    mock_load_job.result.return_value = None

    # Mock the get_table method and its return value
    mock_table = MagicMock()
    mock_table.num_rows = 123  # Simulate the table having 123 rows
    mock_client_instance.get_table.return_value = mock_table

    # Perform the test request
    response = client.post("/data_dump")

    # Assertions
    assert response.status_code == 200
    assert response.json() == {"data": 123}

    # Verify that the mocked methods were called with the expected arguments
    mock_client_instance.load_table_from_uri.assert_called_once_with(
        "gs://gcpmlopsend2end/reviews_all_App.csv",
        "clv-03091991-vertexai.gcpmlops.reviews_all_app",
        job_config=mock_client_instance.load_table_from_uri.call_args[1]["job_config"],
    )
    mock_client_instance.get_table.assert_called_once_with("clv-03091991-vertexai.gcpmlops.reviews_all_app")
