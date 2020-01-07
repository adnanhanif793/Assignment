import requests
import json
import jsonpath

url='http://reqres.in/api/users?page=2'

v_response=requests.get(url)
print(v_response)
v_content=v_response.text
print(v_content)
v_statuscode=v_response.status_code
print(v_statuscode)

v_json_data=json.loads(v_content)
print(v_json_data)

v_per_page=jsonpath.jsonpath(v_json_data,'per_page')
print(v_per_page)

v_data_elements=jsonpath.jsonpath(v_json_data,'data')
print(v_data_elements)
print(len(v_data_elements[0]))

assert v_statuscode==200
assert v_per_page[0]==6
assert v_per_page[0]==len(v_data_elements[0])