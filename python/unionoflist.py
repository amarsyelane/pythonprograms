# Python Program to Find the Union of two Lists
def Union(lst1,lst2):
    rs = list(set(lst1)|set(lst2))
    return rs
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 1]
rs = []
print(Union(lst1,lst2))