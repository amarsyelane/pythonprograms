# Python Program to Merge Two Lists and Sort it

list1 = []
list2 = []
a = int (input('Enter the range : '))
for i in range(1,a):
    num1 = int (input('Enter number : '))
    list1.append(num1)

b = int (input('Enter the range : '))
for i in range(1,a):
    num2 = int(input('Enter number : '))
    list2.append(num2)

list1.extend(list2)
print(list1)
list1.sort()
print(list1)