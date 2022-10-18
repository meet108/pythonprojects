str = "This is string example"
print(len(str))
print(str)
print(str[3::-1] + str[6:4:-1] + str[13:7:-1] + str[21:14:-1])

print(str[0:4][::-1]+str[4]+
      str[5:7][::-1]+
      str[7]+str[8:14][::-1]+
      str[14]+str[15:22][::-1]
      )
