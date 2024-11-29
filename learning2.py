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
