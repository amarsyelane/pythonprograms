

def intersection_list(list1,list2):
    list3 = list(set(list1) & set(list2))
    return list3

list1 = [1,2,3,4,5,6]
list2 = [7,1,8,2,9,3]
print(intersection_list(list1,list2))