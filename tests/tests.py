import lambda_function
from urllib import request, parse, error
import json
from .packages import package_info

expected_return = {
    'statusCode' : 200, 
    'body' : package_info
    }

def test_returned_value_is_not_none():
    val = lambda_function.lambda_handler(None, None)
    assert val is not None

def test_returned_value_is_a_dictionary():
    assert type(lambda_function.lambda_handler(None, None)) is dict

def test_returned_dictionary_value():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    assert expected_return == returned_map

def test_status_code_is_200():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    status_code = returned_map['statusCode']
    assert status_code is not None
    assert status_code == 200

def test_body_has_correct_elements():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    body = returned_map['body']
    assert body is not None
    foundations = body['foundations']
    assert foundations is not None
    packages = body['packages']
    assert packages is not None
    slides = body['slides']
    assert slides is not None

def test_foundations_elements_have_correct_structure():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    body = returned_map['body']
    assert body is not None
    foundations = body['foundations']
    assert foundations is not None
    for k,v in foundations.items():
        assert 'name' in v
        assert 'endpoint' in v
        assert 'visualization' in v

def test_slides_elements_have_correct_structure():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    body = returned_map['body']
    assert body is not None
    slides = body['slides']
    assert slides is not None
    for k,v in slides.items():
        assert 'name' in v
        assert 'endpoint' in v
        assert 'visualization' in v

def test_packages_elements_have_correct_structure():
    returned_map = lambda_function.lambda_handler(None, None)
    assert returned_map is not None
    body = returned_map['body']
    assert body is not None
    packages = body['packages']
    assert packages is not None
    for k,v in packages.items():       
        assert 'description' in v
        assert 'foundations' in v
        assert 'slides' in v
        assert 'default_foundation' in v
        assert 'default_slide' in v
        assert 'slides' in v

def test_remote_package_info_endpoints():
    for remote_context_url_base in lambda_function.remote_package_info_contexts.values():
        remote_package_info_endpoint = parse.urljoin(remote_context_url_base, lambda_function.remote_package_info_endpoint_suffix)

        try:
            remote_endpoint_url = request.urlopen(remote_package_info_endpoint)
            assert remote_endpoint_url is not None
            remote_package_info = json.loads(remote_endpoint_url.read().decode())
            assert remote_package_info is not None
        except error.HTTPError as he:
            assert False
        except error.URLError as ue:
            assert False