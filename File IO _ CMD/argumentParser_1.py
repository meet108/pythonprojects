import sys

if len(sys.argv) > 1:
    a = sys.argv[0]
    b = sys.argv[1]
    c = sys.argv[2]
    print(type(a))
    print(type(b))
    print(type(c))
    print("Argument 1: {}".format(sys.argv[0]))
    print("Argument 2: {}".format(sys.argv[1]))
    print("Argument 3: {}".format(sys.argv[2]))
else:
    print("No arguments passed.")
