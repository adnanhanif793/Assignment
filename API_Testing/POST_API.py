import requests
import jsonpath
import json

url='http://reqres.in/api/users'

#read data from file

f_pointer=open('JsonFiles/Sample-Post-input.json',mode='r')
v_input_data=f_pointer.read()

#convert the data into json/dict
v_input_data_json=json.loads(v_input_data)

print("--------Input Data-----------")
print(v_input_data_json)

v_response=requests.post(url,v_input_data_json)

print("----------API Response--------------")
print(v_response.text)

v_response_code=v_response.status_code
print("--------Response Code---------------")
print(v_response_code)

json_data=json.loads(v_response.text)
print("-----------JSON Data---------------")
print(json_data)

v_id=jsonpath.jsonpath(json_data,'data[0].id')
print("--------ID of student is----------")
print(v_id[0])


assert v_response_code==200