# 0 1 1 2 3 5 8 13
def fibonacci(r):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(2,r):
        next = n1 + n2
        print(next)
        n1 = n2
        n2 = next

r = int (input('Enter the range : '))
fibonacci(r)