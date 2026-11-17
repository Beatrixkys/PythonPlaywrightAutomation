
def assert_conditional_key(condition, key, actual_map, expected_val):
    if condition:
        assert_match_and_log(key, expected_val, actual_map.get(key))
        return True
    return False


def assert_true(condition):
    if not condition:
        raise AssertionError(f'{condition} is not true')

def assert_not_match_and_log(parent, expected_value, actual_value):
    assert expected_value != actual_value, f"Match for {parent}: {expected_value} == {actual_value}"
    
def assert_match_and_log(parent, expected_value, actual_value):      
    assert expected_value == actual_value, f"Mismatch for {parent}: {expected_value} != {actual_value}"
    
def assert_in_and_log(parent, expected_value, actual_value):
    assert expected_value in actual_value, f"{parent}: {expected_value} not in {actual_value}"

def assert_not_none_and_log(parent, actual_value):
    assert actual_value is not None, f"{parent}: {actual_value} is None"

def assert_status_code(response, expected_status):
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Mismatch for {expected_status}:{actual_status}. "
        + ("Could not connect or server error." if actual_status >= 500 else "")
    )
    
def assert_type(parent, expected_type, actual_value):
    """
    Asserts that a value is of the expected type and logs the result.

    Args:
        parent (str): Field or section name for context.
        expected_type (type): The expected Python type.
        actual_value (Any): Value to check.

    Raises:
        AssertionError: If actual_value is not of expected_type.
    """
    assert isinstance(actual_value, expected_type), (f"Expected type:{expected_type}:{type(actual_value)}")


def assert_response_schema(actual, schema, path="response"):
    """
    Validate API response structure and data types against a schema.

    Supported types:
        dict, list, str, int, float, bool, NoneType
    """

    assert isinstance(actual, dict), (
        f"Expected API response to be a dictionary, "
        f"got {type(actual).__name__}"
    )
    for key, expected_type in schema.items():
        assert key in actual, (
            f"Missing field: '{path}.{key}'"
        )
        value = actual[key]
        assert_type(f"{path}.{key}", expected_type, value)
