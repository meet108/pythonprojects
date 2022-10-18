# For loop

# indentation
# 4 spaces
# single tab

for i in range(0, 10, 1):
    print(i)
for i in range(0, 10):
    print(i)
for i in range(10):
    print(i)

# Output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


s = "Hello World"

for x in s:
    print('Current Letter :', x)

# Output
# Current Letter : h
# Current Letter : e
# Current Letter : l
# Current Letter : l
# Current Letter : o

print(range(10))

a = ['Harshal', 'Nimesh', 'Vishal', 'Himanshu', 'Asit']
print(len(a))

for i in range(len(a)):
    print(i, a[i])

    # 0 Harshal
    # 1 Nimesh
    # 2 Vishal
    # 3 Himanshu
    # 4 Asit
