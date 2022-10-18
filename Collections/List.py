ls = [1, 1, "Asit", "Harshal", 'N', 45.5, 45.5, True]

print(ls)
# [1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

print(ls[0])
# 1

print(ls[0:2])
# [1, 1]

print(ls[0:])
# [1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

ls[5] = 66

print(ls)
# [1, 1, 'Asit', 'Harshal', 'N', 66, 45.5]

print(type(ls))
# <class 'list'>


name = [[1, 2, 3, 4, 5, 6], ["Dhairya", "Rahul", "ASit"]]

name[1][1] = 123456
print(name)

print(type(name))
