from db_connection import get_connection
import psycopg2

# dell_store.py
# dell_store.py
def insert_sample_customers():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Remove existing sample customers if any
            cursor.execute("DELETE FROM CUSTOMERS WHERE FIRSTNAME LIKE 'Sample Customer %';")

            # Insert new sample customers
            for i in range(1, 6):
                cursor.callproc(
                    "new_customer",
                    (
                        f"Sample Customer {i}",
                        f"Lastname {i}",
                        f"Address 1 {i}",
                        f"Address 2 {i}",
                        f"City {i}",
                        f"State {i}",
                        12345,
                        f"Country {i}",
                        i,
                        f"sample_email{i}@example.com",
                        "123-456-7890",
                        1,
                        f"CreditCard {i}",
                        "12/25",
                        f"username{i}",
                        f"password{i}",
                        30,
                        60000,
                        "M",
                    ),
                )
            connection.commit()
            print("Sample customers inserted successfully.")
        except psycopg2.Error as e:
            print("Error while inserting sample customers: ", e)
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

