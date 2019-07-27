# Python Program to Print Largest Even and Largest Odd Number in a List.

def evenoddlarge(list):
    even = [num for num in list if num%2 == 0]
    even.sort()
    print("Greatest even number : ",even[-1])
    odd = [num for num in list if num%2!=0]
    print("Greatest odd number : ",odd[-1])
list = [1,2,3,4,5,6,7,8,9,10]
evenoddlarge(list)