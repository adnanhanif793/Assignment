import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

ipAddress=re.compile(r'.[0-255]*.[0-255]*.[0-255]*.[0-255]*.[0-255]*\d')
ip=ipAddress.search('10.121.1.47')
print(ip.group())