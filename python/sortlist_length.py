

def sort_list(list):
    list.sort(key = len)
    return list

list = ['amar','darshan','rushikesh','bunty','raj','nehal','santosh']
print(sort_list(list))