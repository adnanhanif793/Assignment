import requests
import jsonpath
import json

url='http://reqres.in/api/users/2'

f_pointer=open('JsonFiles/Sample-Put-input.json',mode='r')
v_input_data=f_pointer.read()

v_input_data_json=json.loads(v_input_data)

print("--------Input Data-----------")
print(v_input_data_json)

v_response=requests.put(url,v_input_data_json)
print("----------API Response--------------")
print(v_response.text)

v_response_code=v_response.status_code
print("--------Response Code---------------")
print(v_response_code)

json_data=json.loads(v_response.text)
print("-----------JSON Data---------------")
print(json_data)

v_name_input=v_input_data_json['name']
v_job_input=v_input_data_json['job']


print("--------------name in the input file is-------------------------")
print(v_name_input)
print("--------------job in input file is------------------------")
print(v_job_input)

#get data from response file


v_updatedAt=jsonpath.jsonpath(json_data,'updatedAt')

print("---------updateDate in the response-----------")
print(v_updatedAt)


assert v_response_code==200
assert v_updatedAt[0] is not None