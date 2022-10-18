# str = "This is string example"
# print(len(str))
# print(str)
# print(str[1::-1]+
#       str[1:3][::-1]+str[4]+
#       str[4:6][::-1]+str[6]+
#       str[7:9][::-1]+str[9]+
#       str[9:11][::-1]+str[11]+
#       str[11:13][::-1]+str[13]+
#       str[13:16][::-1]+str[16]+
#       str[16:18][::-1]+str[18]+
#       str[18:20][::-1]+str[20]+
#       str[20:22][::-1]
#       )
str = "this is string example"
print(str)
ls = str.split(' ')
a=ls[0][0:2][::-1]+ls[0][2:4][::-1]+" "+ls[1][:2][::-1]+" "+ls[2][0:2][::-1]+ls[2][2:4][::-1]+ls[2][4:7][::-1]+" "+ls[3][0:2][::-1]+ls[3][2:4][::-1]+ls[3][4:6][::-1]+ls[3][6:8][::-1]
print(a)