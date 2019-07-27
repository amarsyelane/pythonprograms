# Python Program to Take in a String and Replace Every Blank Space with Hyphen

def string_replace(string):
    string = string.replace(' ','-')
    print(string)
string = 'i want to become programmer'
string_replace(string)