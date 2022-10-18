try:
    print("outer try block")
    try:
        print("inner try block")
    except:
        print("inner except block")
except:
    print("outer except block")
    