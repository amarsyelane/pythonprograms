
lst = []
l = int(input("enter the length of list : "))
for i in range(l):
    n = int(input('Enter the number : '))
    lst.append(n)
print('Before sorting elements : ',lst)

for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] >= lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
print('After sortion elements : ',lst)