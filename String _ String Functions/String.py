str_ex = 'Softvan_innoventa'

print(str_ex)
# Softvan_innoventa

'''
comment section
comment1
cooment2
'''

print(str_ex[0])
# S

print(str_ex[2:7])
# ftvan

print(str_ex[2:])
# ftvan_innoventa

print(str_ex * 2)
# Softvan_innoventaSoftvan_innoventa

print(str_ex + "Hello")
# Softvan_innoventaHello

print(str_ex, 'hello')
# Softvan_innoventa hello

print(str_ex + '1')
# Softvan_innoventa1

print(str_ex, 1)
# Softvan_innoventa 1

# Format method
print("Hey My name is: %s my roll no is : %d how are you: %s" % ('a', 44, 'Vishal'))

a = 10

b = "Rydham"

print(str(a) + b)

print("%s %d" % (b, a))

print('{},{}'.format(a, b))
