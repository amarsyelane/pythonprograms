
def prime_list(list):
    i = 0
    for i in range(2,len(list)):
        if i%2 == 0:
            print(i)

list = []
n = int (input('Enter the range : '))
for i in range(1,n):
    list.append(i)

prime_list(list)