# Data Comparison Between SQL Table and CSV File

This Python script is designed to perform data comparison between a SQL table and a CSV file. It ensures the data integrity and consistency between the two data sources. The comparison includes checks for row counts, column existence, data types, and values.

## Prerequisites

Before running the script, you need to make sure the following dependencies are installed:

- Python (version X.X.X)
- pytest (version X.X.X)
- pandas (version X.X.X)
- PostgreSQL (version X.X.X) or any compatible database with the 'customers' table.

## Setup

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:

```bash
pip install pytest pandas psycopg2  # You may need to adjust the package names as per your package manager.
```

3. Configure the database connection in the `db_connection.py` file by providing the appropriate credentials.

## Usage

1. Place your CSV file with the data to compare in the location `C:\Users\User\Documents\cust-test.csv`.

2. Run the data comparison script:

```bash
pytest -v test_data_comparison.py
```

## Description

- `fetch_data_from_sql_table`: This function connects to the PostgreSQL database, fetches data from the 'customers' table, and returns a pandas DataFrame.

- `read_data_from_csv`: This function reads data from the CSV file located at `C:\Users\User\Documents\cust-test.csv` and returns a pandas DataFrame.

- `compare_sql_table_to_csv`: This function performs the data comparison between the SQL table and the CSV file. It cleans the data, ensures data types match, and then compares the values in each column.

- `test_data_comparison`: This is the pytest test function that initiates the data comparison using the fixtures.

## Results

- If the data comparison is successful, the script will print "Data comparison successful!" and pass the test.

- If any data mismatches are found, the script will print the details of the mismatches and raise an assertion error, failing the test.

Feel free to modify and adapt this Readme.md to fit your specific use case and project structure. Additionally, make sure to provide relevant information on how to configure the database connection and any other parameters that need to be adjusted.
