
def cout_vow(str):
    cnt = 0
    for char in str:
        if char in 'aeiouAEIOU':
            cnt = cnt +1
    print(cnt)

str = input('Enter the string : ')
cout_vow(str)