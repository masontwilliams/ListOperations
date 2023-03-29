#
# Mason Williams
# 09/19/2021
# Number Analysis Program (Chapter 7, Problem 4)
#

def main():
    # List to store numbers
    number_list = []

    # Variables
    low = 0.0
    high = 0.0
    total = 0.0
    average = 0.0
    number = 0

    # Prompt for numbers
    for i in range(20):
        number = float(input('Enter number ' + str(i + 1) + ' of 20: '))
        number_list.append(number)

    low = min(number_list)
    high = max(number_list)
    total = sum(number_list)
    average = sum(number_list) / len(number_list)

    print (number_list)
    print ('Low:', low)
    print ('High:', high)
    print ('Total:', format(total, ',.2f'))
    print ('Average:', format(average, ',.2f'))

# Call the main function.
main()

