# function without arguement with return "none"
def fn1():
    print("This is User Define function !")
    # none
    return


# function fn1() call
fn1()


# Output: This is User Define function !


# function with single argument without return

def fn2(str):
    print(str)


# function fn2() call
fn2("HELLO WORLD !")


# Output: HELLO WORLD !

# function with multiple arguments without return

def fn3(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)


# function fn3() call
fn3(10, 5)


# 15
# 5
# 50
# 2.0
# 0


# function with no argument with return

def fn4(a, b):
    c = a + b
    d = a - b
    return c, d


# function fn4() call
a, b = fn4(20, 20)
print(a)


# Output:40

def fn5(n):
    if n == 1:
        return 1

    else:
        return n * fn5(n - 1)


n = 5
print(fn5(n))
