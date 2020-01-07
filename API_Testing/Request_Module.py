import requests
#test url
test_url='http://www.techsckool.com/'

#call the request and store the result
v_response=requests.get(test_url)

#print reponse
print(v_response)
print(type(v_response))

#print Status Code
print(v_response.status_code)

#print content
print(v_response.content)

#print response headers
print(v_response.headers)

#print url
print(v_response.url)

#print cookies
print(v_response.cookies)

#prints the encoding used
print(v_data.encoding)

#same as .content but in a more readable format
print(v_data.text)

