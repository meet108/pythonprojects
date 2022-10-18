# how to input in python
# by default input function will return string
# python2=>raw_input()->string input
#             input()-<int input

x = int(input("Enter Integer Value"))

if x < 0:
    x = 0
    """print('Negative changed to zero')"""
    if x == 0:
        print('Zero')
elif x == 1:
    print('Single')
    if x == 0:
        print('Zero')
else:
    print('More')


