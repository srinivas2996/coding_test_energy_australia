import pytest
import great_expectations as ge

@pytest.fixture(scope="module")
def data_batch():
    # Load the CSV file as a batch
    batch_kwargs = {
        "path": r"C:\Users\User\Documents\cust-test.csv",  # Replace with the actual path to your CSV file
        "datasource": "files",
    }
    batch = ge.data_context.DataContext().get_batch(batch_kwargs=batch_kwargs)
    return batch

def test_data_expectations(data_batch):
    # Load an existing expectation suite or create a new one if it doesn't exist
    try:
        expectation_suite = ge.data_context().get_expectation_suite("my_suite")
    except ge.exceptions.exceptions.DataContextError:
        expectation_suite = ge.data_context().suite_edit("my_suite")

    # Define expectations fluently and add them to the suite
    expectation_suite.expect_column_values_to_not_be_null("customerid")
    expectation_suite.expect_column_values_to_be_between("age", min_value=18, max_value=120)
    expectation_suite.expect_column_values_to_be_in_set("gender", ["Male", "Female", "Other"])

    # Save the expectation suite
    expectation_suite.save()

    # Validate the expectation suite against the data batch
    results = data_batch.validate(expectation_suite)

    # Check if the expectations are met
    assert results["success"], "Data expectations not met!"
