supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# for i in enumerate(supplies):
#     print(list(i))

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)
