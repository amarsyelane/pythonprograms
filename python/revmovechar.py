
str = 'abcdefghijklm'
list = []
for i in range(len(str)):
    list.append(str[i])
str2 = ''
for i in range(len(list)):
    if i != 9:
        str2 = str2 + list[i]
print(str2)
