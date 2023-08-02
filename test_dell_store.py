import pytest
import psycopg2
from db_connection import get_connection
from dell_store import insert_sample_customers


@pytest.fixture(scope="module")
def database_connection():
    connection = get_connection()
    yield connection
    connection.close()

def get_filtered_records(database_connection):
    try:
        connection = database_connection
        cursor = connection.cursor()

        # Define the SQL query to fetch the records
        sql_query = """
            SELECT * FROM (
                SELECT CONCAT(c.firstname, ' ', c.lastname) AS cust_fullname, 
                       p.prod_id, 
                       p.title, 
                       p.price
                FROM customers c
                CROSS JOIN products p
            ) AS combined
            WHERE combined.cust_fullname LIKE 'Sample Customer %';
        """

        # Execute the SQL query to fetch the filtered records
        cursor.execute(sql_query)

        # Fetch all the records returned by the query
        records = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()

        return records

    except Exception as e:
        print("Error: ", e)
        return None

def test_insert_and_fetch_sample_customers(database_connection):
    # Insert sample customers
    insert_sample_customers()

    # Fetch the inserted sample records dynamically using an SQL query
    connection = database_connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM CUSTOMERS WHERE FIRSTNAME LIKE 'Sample Customer %';")
    records = cursor.fetchall()

    assert len(records) == 5  # Assuming 5 sample customers were inserted
    # Additional assertions based on the inserted sample records can be performed here


def test_insert_records(database_connection):
    connection = database_connection

    # Get the filtered records using the new function
    filtered_records = get_filtered_records(connection)

    # Perform assertions on the filtered_records
    assert len(filtered_records) > 0
def get_order_counts(connection):
    try:
        cursor = connection.cursor()

        query = """
        SELECT 
            CONCAT(c.firstname, ' ', c.lastname) AS custfullname,
            COUNT(o.orderid) AS order_count
        FROM 
            customers c
        JOIN 
            orders o ON c.customerid = o.customerid
        JOIN 
            orderlines ol ON o.orderid = ol.orderid
        GROUP BY 
            c.customerid, c.firstname, c.lastname
        HAVING 
            COUNT(o.orderid) > 2;
        """

        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        return results

    except Exception as e:
        print("Error: ", e)
        return None


def test_order_counts(database_connection):
    connection = database_connection

    results = get_order_counts(connection)
    assert results is not None

    assert len(results) > 0

    for result in results:
        assert result[1] > 2


if __name__ == "__main__":
    pytest.main(["-v", "test_dell_store.py"])
