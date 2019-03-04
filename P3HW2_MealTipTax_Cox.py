# CTI-110 
# P3HW2 - MealTipTax 
# Damien Cox 
# 3/3/19
#
#Enter the cost of the meal.
cost = int(input('Enter the total cost of the meal: '))

#Calculate the cost of the meal with tax.
wtax = cost * 0.07 + cost

#Enter the amount of a tip.
vtip = int(input('Enter the tip amount for the meal (choose 15, 18 or 20 percent): '))

#Calculate the tip.
wtip = vtip/100 * wtax + wtax



#Display results.
print('Total meal cost is $', format(wtip, ',.2f'))
print ("\n" * 1)
print('Pre tax: $', format(cost, ',.2f'))
print('After tax: $', format(wtax, ',.2f'))
print('With tip: $', format(wtip, ',.2f'))
print ("\n" * 1)



