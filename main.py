# Learncs.org
# 1: Printing
print("Hello!!!")

# 2: Variables
# floats, ints, strings
myint = 7
print(myint)

myfloat = float(7)
print(myfloat)

mystring = "hello"
mystring2 = 'hello'
print(mystring + " " + mystring2)

mychar, mychar2 = "one", "two"
print(mychar, mychar2)

# 3: Lists (Basic)
# can contain any object, can be any size
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0], mylist[1], mylist[2])

# 4: Basic Operators
# follows PEMDAS
# %: returns remainder
# ** power
# can muiltiply strings
# lists support operators
number = 2 + 3 * 9 / 3
print(number)

modulo = 11 % 3
print(modulo)

power = 2 ** 3
print(power)

manywords = "word" * 10
print(manywords)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
print(list1 + list2)

print([1,2,3] * 3)

# 5: String Formatting
# Python uses C-style formatting
# s for strings
# d for integers
# f for floats or %.<ofdigitstotheright>f

name = "Keegan"
name2 = "Smith"
print("Hello, %s %s!" % (name, name2))

debt = 25.67893
print("You owe me $%.2f." % debt)

fine = 15
print("Pay soon or owe me $%d." % fine)

# 6: Basic String Operations
# len() returns length of string
# .index("") returns index of char in string (first instance)
# .count returns # of chars in string
# use [start:end:step] to print section of string
# .upper() makes all chars uppercase
# .lower() makes all chars lowercase
# .startswith("") returns true if string starts with input
# .endswith("") returns true if string ends with input
# .split("") splits strings into a list at input


ghost = "Spooky Boo"
print(len(ghost))
print(ghost.index("B"))
print(ghost.index("o"))
print(ghost.count("o"))
print(ghost[2:8])
print(ghost[1:10:2])
print(ghost[::-1])
print(ghost.upper())
print(ghost.lower())
print(ghost.startswith("Spooky"))
print(ghost.endswith("Boo"))
print(ghost.split("k"))