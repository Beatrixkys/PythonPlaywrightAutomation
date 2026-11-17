from pages import api_page
from schemas import api_schemas
from utils import assert_utils
import pytest

@pytest.mark.api
def test_api(api_client):
    response_code, response=api_page.call_get_posts_api(api_client, parameters={"postId": 1})
    assert_utils.assert_status_code(response_code, 200)

    for entry in response:
        assert_utils.assert_response_schema(entry, api_schemas.POSTS_SCHEMA)