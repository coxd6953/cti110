# Meal Tip Calculator
# 3/3/19
# CTI-110 P2HW2 - Meal Tip Calculator
# Damien Cox
#
#Enter the cost of the meal.
cost = int(input('Enter the total cost of the meal: '))

#Calculate the amount of the following tip percentages: 15%, 18% and %20.
fifteen = .15 * cost
eighteen = .18 * cost
twenty = .20 * cost

#Display results.
print('A 15% tip on a bill of $', cost, 'is $', format(fifteen, ',.2f'))
print('A 18% tip on a bill of $', cost, 'is $', format(eighteen, ',.2f'))
print('A 20% tip on a bill of $', cost, 'is $', format(twenty, ',.2f'))
