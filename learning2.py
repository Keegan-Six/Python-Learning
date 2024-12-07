import module
import sys
import numpy as np
import pandas as pd
# 8: Loops
# 'for' and 'while' loops work similiar to other languages
# can iterate over numbers using range() and xrange()
# range returns list, xrange returns iterator
# range(start,end,step)
# use 'break' to exit loop, use 'continue' to exit current iteration of loop
# unlike other languages, can use 'else' with loops
names = ["Keegan", "Jake", "Hal"]

for names in names:
    print (names)

for x in range(0,5):
    print(x)

count = 0
# skips 3
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
else:
    print ("count reached %d" %(count))

# 9: Functions
# use 'def'+ "function name"(arguments):
# simply call a function by typing "function name"(arguments)

def addition(number1, number2):
    return number1 + number2

print(addition(1,2))

# 10: Classes and Objects
# Classes are a template to create your object
# Objects are varibles and functions in a single entity
# you can assign a class to an object
# access features from a class by doing 'object'.
# the __init__() is a special function that is called when the class is initated, used for assigning values
class MyClass:
    variable = 10
    def __init__(self,number):
        self.number = number
    
    def function(self):
        print("message")
    
    def returnnum(self):
        return self.number
    
myobject = MyClass(7)
print(myobject.variable)
myobject.function()
print(myobject.returnnum())

# 10: Dictionaries
# works with keys and values instead of indexes
phonebook = {
    "Keegan" : "319-720-5878",
    "Jack" : "540-870-3408",
    "Catherine" : "319-000-234"
}
del phonebook["Keegan"]

for name, number in phonebook.items() :
    print("Phone number of %s is %s" % (name,number))
    
# 11: Modules
# Modules allow you to seperate code into different files
# use import command

module.function()

# 12: Numpy Arrays
# requires import, import numpy
# may have to change PATH variable
# good for element-wise calculations
# allows subsetting

height = [1.8, 1.7, 1.76, 1.89]
weight = [81.32, 90.25, 78.31, 88.92]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)

print(bmi[bmi > 25])

# 13 List Comphrehensions
# creates a new list, based on specific specifications, from an old list

numbers = [ -80, -40, -4, 0, 3, 4, 12, 18]
muiltiple4 = [number for number in numbers if number % 4 == 0]
positive = [number for number in numbers if number > 0]
print(positive)

# 14 Lambda Functions
# can be defined in one line
# useful for simple functions

sum = lambda x, y : x + y
print(sum(6,7))

l = [2,3,6,9,12,14]
lodd = []
for i in l :
    odd = lambda x : (x % 2) == 1
    lodd.append(odd(i))
print(lodd)

# 15 Muiltiple Function Arguments
# it is possible to create functions with a variable number of elements with *argument
# it is possible to create functions with keywords, with **argument

def sumall(*all) :
    sum = 0
    i = 0
    alllist = list(all)
    while i < len(alllist) :
        sum = sum + alllist[i]
        i = i + 1
    return sum
sumall(3,4,5,6,7,8,9)

def math(number1, number2, **option) :
    if option.get("action") == "sum" :
        print(number1 + number2)
    if option.get("action") == "divide" :
        print(number1 / number2)
    if option.get("retrieve") == "first" :
        return number1
    if option.get("retrieve") == "second" :
        return number2

print(math(1,3, action = "sum", retrieve = "second"))
