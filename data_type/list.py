'''
(1) Orderd
(2) Allow Duplicate
(3) Mutable
'''


# decleare
list1 = [1, 2, 3, 4, 5]
print(list1)


# append
list1.append(6)
print(list1)


# access
print(list1[0])


# update
list1[0] = 100
print(list1)


# sort
list1.sort()
print(list1)


# insert
list1.insert(0, 0)
print(list1)


# resverse
list1.reverse()
print(list1)


# sort with reverse
list2 = [10, 5, 25, 70, 40, 35]
list2.sort(reverse = True)
print(list2)


# extend
list1.extend(list2)
print(list1)


# casting
my_set = set(list1)
my_tuple = tuple(list1)



# iteration
# --> For loop

list3 = ["Rohan", "Ram", "Raja", "Rahul", "Raj"]

for item in list3:
    print(item)



# --> while loop

i = 0
while i < len(list3):
    print(list3[i])
    i += 1

    
    
# --> Add tuple in the list

list4 = ["India", "Chaina", "UK", "PAK"]
my_tuple = (1, 2, 3, 4)
list4.append(my_tuple)
print(list4)

    
# Question of list:

'''
Question 1:
Given a list of tuples, write a Python function to convert this list into a dictionary
where the first element of each tuple is the key and the second element is the value.
'''

def list_to_dict(lst):
    my_dict = []
    
    
lst = [('a', 1), ('b', 2), ('c', 3)]

my_dict1 = dict(lst)


# add dictionary in list
list1.append(my_dict1)
print(list1)



# convert dictionary to list
my_list2 = my_dict1.items()
print(my_list2)



# list to dictionary
my_dict2 = dict(my_list2)
print(my_list2)



# Write a Python function to add elements from a set and a tuple to a list.

def add_tuple_set_in_list(lst, s, t):
    lst.extend(s)
    lst.extend(t)
    print(lst)
    
lst = [1, 2, 3]
s = {4, 5, 6}
t = (7, 8, 9)
add_tuple_set_in_list(lst, s, t)
