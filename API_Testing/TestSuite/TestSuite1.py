import requests
import json
import jsonpath

def test_getAPI():
    url = 'http://reqres.in/api/users?page=2'

    v_response = requests.get(url)
    v_content = v_response.text
    v_statuscode = v_response.status_code
    v_json_data = json.loads(v_content)
    v_per_page = jsonpath.jsonpath(v_json_data, 'per_page')
    v_data_elements = jsonpath.jsonpath(v_json_data, 'data')
    assert v_statuscode == 200
    assert v_per_page[0] == 6
    assert v_per_page[0] == len(v_data_elements[0])


def test_deleteAPI():
    url = 'http://reqres.in/api/users/2'

    response = requests.delete(url)
    v_sc = response.status_code
    v_data = response.text
    assert v_sc == 204
    assert len(v_data) == 0