import requests
import json
import jsonpath

url='http://reqres.in/api/users/2'

response=requests.delete(url)
v_sc=response.status_code

print(v_sc)
v_data=response.text
print(v_data)

assert v_sc==204
assert len(v_data)==0