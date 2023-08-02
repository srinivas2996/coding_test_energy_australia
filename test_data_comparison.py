import pytest
import pandas as pd
from db_connection import get_connection

def fetch_data_from_sql_table(connection, table_name):
    try:
        # Connect to the database and fetch data from the specified table
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM customers;")
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        cursor.close()

        # Convert the data into a pandas dataframe
        df = pd.DataFrame(data, columns=columns)

        # Convert the 'income' column to integer type
        df['income'] = df['income'].astype(int)

        return df

    except Exception as e:
        print("Error: ", e)
        return None


def read_data_from_csv(csv_file):
    try:
        # Read data from the CSV file and convert it into a pandas dataframe
        df = pd.read_csv(r"C:\Users\User\Downloads\cust-test.csv")

        # Clean the data by stripping whitespaces from string columns
        string_columns = df.select_dtypes(include='object').columns
        df[string_columns] = df[string_columns].apply(lambda x: x.str.strip())

        return df

    except Exception as e:
        print("Error: ", e)
        return None


# ... (Other functions as before) ...

# test_data_comparison.py

def compare_sql_table_to_csv(database_connection):
    def compare_sql_table_to_csv(database_connection):
        # Fetch data from the SQL table and convert it to a dataframe
        sql_table_name = "customers"  # Replace with your actual SQL table name
        sql_df = fetch_data_from_sql_table(database_connection, sql_table_name)

        # Read data from the CSV file and convert it to a dataframe
        csv_file_path = r"C:\Users\User\Downloads\cust-test.csv"  # Replace with your actual CSV file path
        csv_df = read_data_from_csv(csv_file_path)

        # Ensure data types match before comparison
        csv_df['income'] = csv_df['income'].astype(int)

        # Print the row counts for debugging
        print("SQL DataFrame row count:", len(sql_df))
        print("CSV DataFrame row count:", len(csv_df))

        # Print the unique values of a primary key or unique identifier column
        primary_key_column = "customerid"  # Replace with your actual primary key column name
        print("Unique values in SQL DataFrame:", sql_df[primary_key_column].nunique())
        print("Unique values in CSV DataFrame:", csv_df[primary_key_column].nunique())

        # Compare the number of rows in both dataframes
        assert len(sql_df) == len(csv_df), f"Row count mismatch. SQL: {len(sql_df)}, CSV: {len(csv_df)}"

        # Compare column by column
        for column_name in sql_df.columns:
            assert column_name in csv_df.columns, f"Column '{column_name}' missing in CSV."
            if not sql_df[column_name].equals(csv_df[column_name]):
                print(f"Data mismatch in column '{column_name}':")
                print("SQL DataFrame:")
                print(sql_df[column_name])
                print("CSV DataFrame:")
                print(csv_df[column_name])
                assert False, f"Data mismatch in column '{column_name}'."

        # Compare primary key or unique identifier column
        assert sql_df[primary_key_column].equals(csv_df[primary_key_column]), "Primary key column mismatch."

        # If all assertions pass, the data comparison is successful
        print("Data comparison successful!")


@pytest.fixture(scope="module")
def database_connection():
    connection = get_connection()
    yield connection
    connection.close()

def test_data_comparison(database_connection):
    compare_sql_table_to_csv(database_connection)