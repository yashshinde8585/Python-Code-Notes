'''
Dictionary
1 Represent a group of object as key-value pair 
2 syntax: dic_name = { key: value }
3 Indexing and slicing not work
4 Insertion order is preserved 
5 Hetrogenous elements are allowed 
6 Mutable in nature 
7 key must be unique but duplicates value are allowed 
8 Unordered, mutable and (don't allow duplicate keys) 
'''

#Basic syntax of a dictionary 
'''example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
print(example)'''

#The value can be any data types and can be duplicated
'''dict_demo = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik",
    "num": 21
}
print(dict_demo) 
#op:{'Name': 'Yash', 'age': 21, 'add': 'Nashik', 'num': 21}
'''

# get(): Returens the value of specified key(return key according to value)
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik"
}
Age = dict_info.get("age")
print(Age) #op: 21
'''

#items(): return all (key-value) pairs as tuple
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik"
}
info = dict_info.items()
print(info)
#op: dict_items([('Name', 'Yash'), ('age', 21), ('add', 'Nashik')])
'''

#keys(): returns all keys 
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "city": "Nashik"
}
print(dict_info.keys())''' 
#op: dict_keys(['Name', 'age', 'city'])

# values(): retruns all values in dictionary
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik"
}
print(dict_info.values())''' 
#op: dict_values(['Yash', 21, 'Nashik'])

# pop(): removes a key-value from the dictionary (specify the key inside its parentheses) 
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "city":"Nashik",
}
dict_info.pop("city")
print(dict_info)'''
#op: {'Name': 'Yash', 'age': 21}

# popitem(): work like pop() difference is that removes the last item in dictionary
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "city": "Nashik",
    "Gender": "Male"
}
dict_info.popitem()
print(dict_info)'''
#op: {'Name': 'Yash', 'age': 21, 'city': 'Nashik'}

# update(): inserts the specified item to dictionary (adds an items to dict)
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik",
    "Gender": "Male"
}
dict_info.update({"age":22})
print(dict_info)'''
#op: {'Name': 'Yash', 'age': 22, 'add': 'Nashik', 'Gender': 'Male'}

# copy(): does what its name implies - its copies the dictionary into the variable specified
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik",
    "Gender": "Male"
}
another = dict_info.copy()
print(another)'''
#op: {'Name': 'Yash', 'age': 21, 'add': 'Nashik', 'Gender': 'Male'}

# clear(): removes all the entries in the dictionary 
'''dict_info = {
    "Name":"Yash",
    "age": 21,
    "add": "Nashik",
    "Gender": "Male"
} 
dict_info.clear()
print(dict_info)''' 
#op: {}