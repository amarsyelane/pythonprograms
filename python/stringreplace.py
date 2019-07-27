
def stringreplace(string):
    string = string.replace('a','$')
    return string

string = input('Enter the string : ')
print(stringreplace(string))