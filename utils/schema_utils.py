
from utils import assert_utils


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
        assert_utils.assert_type(f"{path}.{key}", expected_type, value)
