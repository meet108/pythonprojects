# Dictionary functions

dict = {'Name': 'Abc', 'Age': 18}
print(len(dict))
# 2

asit = {'Name': 'Abc', 'Age': 18}
print(type(asit))
# <class 'dict'>


a = str(dict)
print(a[1])
# {'Name': 'Abc', 'Age': 18}

print(type(str(dict)))
# <class 'str'>

dict = {'Name': 'Abc', 'Age': 7}
print(len(dict))
# 2
dict.clear()

print(len(dict))
# 0

dict1 = {'Name': 'Abc', 'Age': 7}
abc = dict1.copy()
print(abc)
# {'Name': 'Abc', 'Age': 7}

tupl = ('name', 'age')
the = dict.fromkeys(tupl)
print(the)
# {'name': None, 'age': None}

dict = dict.fromkeys(tupl, 10)
print(dict)
# {'name': 10, 'age': 10}

dict = {'Name': 'abc', 'Age': 7}
print(dict.get('Age'))
# 7

print(dict.get('Education', "Never"))
# Never

dict = {'Name': 'Abc', 'Age': 7}
print(dict.items())
# ls=dict_items([('Name', 'Abc'), ('Age', 7)])

print(dict.values())
# dict_values(['Abc', 7])

print(dict.keys())
# dict_keys(['Name', 'Age'])


dict1 = {'Name': 'xyz', 'Age': 7}
dict2 = {'Gender': 'male'}
dict1.update(dict2)
print(dict1)
print(dict2)
# {'Name': 'xyz', 'Age': 7, 'Gender': 'male'}
