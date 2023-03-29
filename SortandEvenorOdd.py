#Mason Williams
#09/19/2021

import random


firstList = []


for j in range(10):
    firstList.append(random.randint(1,50))

print("List: ", firstList)

firstList.sort()
print("Sorted list: ", firstList)

for n, i in enumerate(firstList):
    if i%2 == 0:
       firstList[n] = "Even"
    else:
       firstList[n] = "Odd"

print("List of if each number is even or odd: ", firstList)
