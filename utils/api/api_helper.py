import constant as constant
from urllib.parse import urlencode

def get_headers(extra_headers, override_all=False):
    """
    Builds headers for a request.
    Args:
        token (str): Bearer token for Authorization.
        override_all (bool): If True, skip default headers.
        **overrides: Extra headers to add or replace.
    Returns:
        dict: Final headers.
    """
    headers = {} if override_all else constant.AUTH_HEADERS.copy()
    if extra_headers:
        headers.update(extra_headers)
    return headers

def parse_response(response):
    """
    Handles a response object to return type
    Args:
        response: Reponse from API call
    Returns:
        -JSON : if valid JSON
        -Str : plain text
    """
    try:
        data = response.json()
        return data
    except ValueError:
        data = response.text
        return data
    
def construct_url(base_url, endpoint, params=None):
    """
    params: dict or list of tuples for query parameters
    """
    if params:
        return f"{base_url}{endpoint}?{params}"
    return f"{base_url}{endpoint}"
