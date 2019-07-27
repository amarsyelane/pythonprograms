def divmulnums(list):
    for n in range(len(list)):
        if n%5 == 0 and n%7 == 0:
            print(n)

list = []
for i in range(1,100):
    list.append(i)
divmulnums(list)