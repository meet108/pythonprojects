# # 1)
# a=10
# b=0
#
# try:
#     print("Outer Try Block")
#     try:
#         print("Nested Try Block")
#         print(a/b)
#     except TypeError:
#         print("Nested Except Block")
# except ZeroDivisionError:
#     print("Outer Except Block")
#     print("Zero Division")
# 2)
# a=10
# b=5.2
#
# try:
#     print("Try Block")
#     print(int(a / b))
# except TypeError:
#     print("1 Except Block")
# except ZeroDivisionError:
#     print("2 Except Block")
# finally:
#     print("Close All")
# 3)
def divide(x,y):
    try:
        print(f'{x}/{y} is {x/y}')
    except ZeroDivisionError:
        print("Zero Divison")
    finally:
        print("Close All")
    else:
        print("divide() worked fine.")

divide(10,2)
divide(5,0)
# # 4)
# a=10
# b=0
# try:
#     print("Outer Try")
#     print(a/b*a)
#     try:
#         print("Nested Try")
#         print(a/b)
#     except ZeroDivisionError:
#         print("Nested Except")
#     finally:
#         print("Nested Finally")
# except ArithmeticError:
#     print("Outer Except")
# finally:
#     print("Outer Finally")
#
#
#