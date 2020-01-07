

import jsonpath
import json

v_pointer=open('JsonFiles/sample-json.json', mode='r')

data=v_pointer.read()
print(data)
print(type(data))

json_data=json.loads(data)  #reads string data and converts to dictionary
print(json_data)
print(type(json_data))

d1=jsonpath.jsonpath(json_data,'City')
d2=jsonpath.jsonpath(json_data,'Class')
d3=jsonpath.jsonpath(json_data,'School')
d4=jsonpath.jsonpath(json_data,'Students')
d5=jsonpath.jsonpath(json_data,'Students[0]')
d6=jsonpath.jsonpath(json_data,'Students[0].Name')
d7=jsonpath.jsonpath(json_data,'Students[0,1,2].Name')
d8=jsonpath.jsonpath(json_data,'Students[0:2].Name')
d9=jsonpath.jsonpath(json_data,'Students[*].Name')
d10=jsonpath.jsonpath(json_data,'Students[0:-1].Name')


print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print(d8)
print(d9)
print(d10)

assert d10[0]=='Sohan'
assert d10[0]=='Abhay'


