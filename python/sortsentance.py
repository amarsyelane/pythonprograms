
def sort_sent(snt):
    wrds = snt.split(" ")
    wrds.sort()

    newsnt = " ".join(wrds)

    return newsnt

snt = input('Enter the sentance : ')
print(sort_sent(snt))