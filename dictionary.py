# Dictionary

'''
1. mutable
2. orderd
3. There is not a duplicate key
'''

# decleare 
dict1 = {
    "phy" : 98,
    "chem" : 99,
    "maths" : 95
}
print(dict1)

# access
print(dict1["phy"])

# insert
dict1["English"] = 94


# update
dict1["English"] = 100


# remove
del dict1["maths"]
value = dict1.pop("maths", 100)
print(dict1)


# change the key name
dict1["Hindi"] = dict1.pop("English")


# decleare data as list & tuple
dict2 = {
    "marks" : [98, 97, 95],
    "subject" : {"phy", "chem", "maths"}
}
print(dict2["marks"])


# iterate of the dictionary ------> output will be only keys

for item in dict1:
    print(item)


# oiterate of the dictionary ------> output will be only key and value
for key, value in dict1.items():
    print(key, value)


# check key is exist or not

for key in dict1:
    if key in dict1:
        print("Yes Present")
        break
    else:
        print("Not present")

