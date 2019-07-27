
num = int(input('Enter the number : '))
arm = 0
dup = num
while dup != 0:
    rem = dup % 10
    arm += rem**3
    dup = dup // 10

if num == arm:
    print('it is armstrong number')
else:
    print('not armstrong number')