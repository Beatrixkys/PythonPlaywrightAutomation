

import constant
from utils.api import api_helper

def build_get_param(search_parameters):
    parameters = {
        "postId": search_parameters,
    }
    return parameters

def call_get_posts_api(api_client, parameters=None, auth_headers=None):
    get_client = api_client(base_url = constant.BASE_API_PLACEHOLDER)
    get_response = get_client.get(constant.POSTS_ENDPOINT, parameter=parameters)
    parsed_get_response = api_helper.parse_response(get_response)
    return get_response, parsed_get_response

def call_get_comments_api(api_client, parameters=1, auth_headers=None):
    parameters = build_get_param(parameters)
    get_client = api_client(base_url = constant.BASE_API_PLACEHOLDER)
    get_response = get_client.get(constant.COMMENTS_ENDPOINT, parameter=parameters)
    parsed_get_response = api_helper.parse_response(get_response)
    return get_response, parsed_get_response