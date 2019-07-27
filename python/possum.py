# Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List

def posadd(list):
    neg = [num for num in list if num < 0]
    print(neg)
    epos = [num for num in list if num%2==0 and num > 0]
    print(epos)
    opos = [num for num in list if num%2!=0 and num > 0]
    print(opos)
list = [-1,-2,-3,-4,-5,1,2,3,4,5,6,7,8,9,10]
posadd(list)