                                                                            # Python Program to Count the Number of Each Vowel
def count_vow(str):
    cnt = 0
    for char in str:
        if char in 'aeiouAEIOU':
            cnt = cnt + 1
    return cnt

str = input('Enter the string : ')
print(count_vow(str))