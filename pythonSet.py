# list, tuple, set, dictionary

# set: a collection, unordered, unchangeable, unidexed

# create a set
thisSet = {"apple", "banana", "cherry"}
print(f"thisSet: {thisSet}")

# what is Unordered? the items in a set do not have a defined order. 
# Duplicates Not allowed
# my_set = set(my_list)
# if my_list = [1, 2, 3, 3, 4, 4, 5]
# my_set = {1, 2, 3, 4, 5}
# how to remove the duplicated value? -> discard() and remove()

thisSet = {"apple", "banana", "cherry", "apple"}
print(f"thisSet: {thisSet}")

# the values True and 1 are consided the same value in sets and are treated as duplicates
# True = 1 in a Set
thisSet = {"apple", "cherry", True, 1, 2}
# the expected return: True, cherry, 2, apple
# 1 cannot be returned because True and 1 are same. 
print(f"True and 1 check(thisSet): {thisSet}")

"""
get the length of a set
len(): list, tuple, strings, dictionaries, byteArrays?
generators and ranges(other interable objects)
"""
print(f"len(thisSet): {len(thisSet)}")

"""
String, int and boolean data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
"""

# can be contain different data types
set1 = {
    "abc",
    34, 
    True, 
    40,
    "male"
}
mySet = {
    "apple",
    "banana",
    "cherry"
}

print(f"set1 with different data types: {set1}")
print("print datatype of set1: ", type(set1))
print("print datatype of mySet: ", type(mySet))
# expected return: <class 'set'>
# sets are defined as objects with the dat type 'set'

"""
using the set() constructor to make a set:
thisSet = set("apple", "banana", "cherry")
print(thisSet)
"""
