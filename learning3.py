# 16 Exception Handling
# handles errors, similiar to other languages
# use try, except block
# except "errorname" :

numbers = [1,2,4,5]

for i in range(6) :
    try :
        print(numbers[i])
    except IndexError: 
        print("error")

# 17 Sets
# Sets are lists with no duplicates
# intersection, find elements between two sets that appear in both
# symmetric_difference, find elements that only appear in one set
# difference, find elements that only appear in one set and not the other
# union, find all elements in both sets

print(set("my name is Keegan and Keegan is my name".split()))
set1 = set([1,2,2,3,4,5,6,6,7,8,9,10,10])
set2 = set([1,4,7,9])
print("numbers in both : %s" % set1.intersection(set2))
print("numbers in only one : %s" % set1.symmetric_difference(set2))
print("numbers in set 2 but not set 1: %s" % set2.difference(set1))
print("all numbers: %s" % set1.union(set2))

# 18 Serialization
# python has json decoding and encoding libraries
# two types, object and string
# object: lists and dictionaries nested inside each other
# object, allows one to use python methods to edit
# string: pass data into other program, or load into datastructure

import json
# encoding
json.string = json.dumps([1,2,3,"a","b","c"])
# loading
print(json.loads(json.string))

# 19 Code Introspection

    
















