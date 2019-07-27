
def interest(pi,years,rate):
    return (pi*years*rate)/100

pi = int(input('Enter the principal amount : '))
years = int(input('Enter the years : '))
rate = int(input('Enter the rate of interest : '))
print(interest(pi,years,rate))