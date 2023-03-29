# Mason Williams
# 09/19/2021


import random


firstList = []
secondList = []
thirdList = []


for j in range(6):
    firstList.append(random.randint(1,19))

print("First list: ", firstList)

for i in range(6):
    secondList.append(random.randint(4,18))

print("Second List: ", secondList)

print("The larger number in each comparison:")
for j in zip(firstList):
    for i in zip(secondList):
        if j > i:
            print("First list")
        elif j < i:
            print("Second list")
        else:
            print("Equal")

for k in secondList:
    firstList.append(k)

print("Combined list: ", firstList)
print("First three elements: ", firstList[:3])
print("Last three elements: ", firstList[-3:])
