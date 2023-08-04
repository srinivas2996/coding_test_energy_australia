# test_expectations.py
import pytest
import great_expectations as ge

@pytest.fixture
def read_csv_file():
    # Load the CSV file using great_expectations
    return ge.read_csv(r"C:\Users\User\Documents\cust-test.csv")

def test_expect_column_values_not_to_be_null(read_csv_file):
    result = read_csv_file.expect_column_values_to_not_be_null("customerid")
    assert result.success, f"Column 'customer_id' has null values"

def test_expect_column_values_to_be_between(read_csv_file):
    result = read_csv_file.expect_column_values_to_be_between("age", min_value=10, max_value=100)
    assert result.success, f"Column 'age' has values outside the specified range"

def test_expect_column_values_to_be_in_set(read_csv_file):
    result = read_csv_file.expect_column_values_to_be_in_set("gender", ["M", "F", "Other"])
    assert result.success, f"Column 'gender' has values not in the specified set"
