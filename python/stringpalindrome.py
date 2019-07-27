# Python Program to Check if a String is a Palindrome or Not

str = input('Enter the string :')
if str == str[::-1]:
    print('string is palindrome')
else:
    print('string not a palindrome')