# def inner1(func):
#     def inner2():
#         print("Before Function Execution")
#         func()
#         print("After Function Execution")
#     return inner2
# @inner1
# def function_to_be_used():
#     print("This is inside the function")
# function_to_be_used()
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)