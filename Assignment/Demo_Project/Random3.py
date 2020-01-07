'''spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham'''

import pprint
#to count the number of all character
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

'''for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)'''

for i in message:
    count[i]=count.get(i,0)+1
#print(str(count))

for k,v in sorted(count.items()):
    print(k,'=',v)