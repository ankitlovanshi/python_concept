    # set
'''
1. Unordered, 
2. not allows duplicates
3. we can not access and change ele using indexing
4. it can store int, string, tuple 
5. it can't store list, dictionary becouse it is mutable
6. union, intersection, Symmetric

'''

# create
set1 = {101, 102, 103, 104, 105}


# create a set with string
set2 = {'a', 'b', 'c', 'd'}


# create a set with mix data
set3 = {101, "Rohan", 'a', -2}

# empty set
set4 = set()


# type casting
my_list = list(set2)
my_tuple = tuple(set2)


# add element
set1.add(100)
print(set1)


# update--->(we can update only iterable object)
set1.update(set2)
print(set1)


# union
my_set1 = {2, 9, 1, 8}
my_set2 = {1, 7, 3, 2}
print(my_set1.union(my_set2))


# intersection (comman element)
print(my_set1.intersection(my_set2))


# diffirence between 2 list
print(my_set1.difference(my_set2)) # {8, 9}
print(my_set2.difference(my_set1)) # {7, 3}


# symmetric_difference
print(my_set1.symmetric_difference(my_set2)) # {3, 7, 8, 9}


