# coding_test_energy_australia
Dell Store Database Testing
This repository contains a Python script to interact with the sample 'Dell' store database and perform tests using pytest. The script connects to the database, fetches records, and executes tests to validate the database operations.

Requirements
To run the code in this repository, you will need the following:

Python (version 3.6 or higher)
pytest (version 6.0 or higher)
psycopg2 (PostgreSQL adapter for Python)
Installation
Clone the repository to your local machine.
Install the required dependencies by running: pip install pytest psycopg2
Usage
Ensure that you have a PostgreSQL database named 'dellstore' with proper credentials and schema.
Modify the 'db_connection.py' file to provide the correct database credentials if necessary.
Run the 'test_dell_store.py' script to execute the test cases.
Files
test_dell_store.py: Contains the test cases to interact with the 'dellstore' database.
db_connection.py: Provides the function to establish a connection to the database.
dell_store.py: Contains functions to insert sample customers into the 'CUSTOMERS' table.
Test Cases
test_insert_and_fetch_sample_customers: This test case checks if the sample customers were inserted successfully into the 'CUSTOMERS' table and fetches the inserted records.
test_insert_records: This test case checks if the get_filtered_records function can fetch filtered records from the database and verifies that the filtered records are not empty.
test_order_counts: This test case checks if the get_order_counts function can correctly fetch the order counts for customers with more than 2 orders and verifies that the query returns results.
Note
Ensure that you have set up the PostgreSQL database and configured the connection details correctly in 'db_connection.py' before running the test cases. The tests may fail if the database is not accessible or the sample customers are not inserted correctly.
