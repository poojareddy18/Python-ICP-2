lbs = []
kgs = []
total = int(input("Enter the number of students:"))
for i in range(total):
    num = int(input('Enter the weights:'))
    lbs.append(num)
    kilograms = num * 0.454
    kgs.append(round(kilograms))
print(lbs,kgs)