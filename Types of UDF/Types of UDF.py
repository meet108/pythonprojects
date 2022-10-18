#   Function Arguments:

#   1)  Required arguments
#   2)  Keyword arguments
#   3)  Default arguments
#   4)  Variable-length arguments
#	5)	Dictionary arguments
#   6)  Lamda Function

#   1) Required arguments:

# Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function definition.


def fn1(a):
    print(a)


fn1("Hello World")


# Output:Hello World


#   2) Keyword arguments:

# Keyword arguments are related to the function calls.
# When you use keyword arguments in a function call,
# the caller identifies the arguments by the parameter name.

def fn2(str):
    print(str)


fn2(str="Good Evening")


# Output:Good Evening


#   3)  Default arguments:

#       A default argument is an argument that assumes a default value
#       if a value is not provided in the function call for that argument,it prints default value if it is not passed

def fn3(name, marks=35):
    print("Name=", name)

    print("Marks=", marks)


fn3(marks=50, name="XYZ")

# Output:

#	Name=XYZ
#	Marks=50

fn3(name="ABC")


# Output:

#	Name=ABC
#	Marks=35


#   4)  Variable-length arguments

#       You may need to process a function for more arguments than you specified while defining the function.
#       These arguments are called variable-length arguments and are not given in the function definition,

#       An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.
#       This tuple remains empty if no additional arguments are specified during the function call.

def fn4(*tuplevar):
    print(type(tuplevar))
    print(tuplevar)

fn4(50)
# Output:50
fn4("string", 70, "Hello", "disha", "rushika", "smit")


# Output:
#	60
#	70
#	Hello


#	5)	Dictionary arguments

# #A keyword argument is where you provide a name to the variable as you pass it into the function.
# #One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
# #That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
def fn5(**std):
    print(std)
    print(type(std))
    if std is not None:
        for key, value in std.items():
            print("%s = %s" % (key, value))

fn5(fn='Abc', ln='Def', name="Yash", demo="Hemil")

# Output:
#	fn=Abc
#	ln=Def

# lambda function=>anonymous function
"""
to execute your single line business logic
"""
square = lambda x: x * x
print(square(15))

addition = lambda x, y: x + y
print(addition(15, 25))
old_list = [1, 2, 3, 4, 5]
# ls = []
# for i in old_list:
#     ls.append(i * 2)

new_list = list(map(lambda x: x * 2, old_list))
print(new_list)

old_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda x: (x % 2 == 0), old_list))
print(new_list)