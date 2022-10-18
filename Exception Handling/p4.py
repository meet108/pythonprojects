try:
    print("outer try block")
except:
    print("first except block")
except:
    print("second except block")
finally:
    print("finally block")