

def remove_pun(str):
    p = '''! () - []{};:'"\,<>./?@#$%^&*_~'''
    for i in str.lower():
        if i in p:
            str = str.replace(i,"")
    print(str)

str = input('Enter the string with any puctuations symbols : ')
remove_pun(str)