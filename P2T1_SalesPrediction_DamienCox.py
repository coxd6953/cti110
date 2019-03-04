# Sales Profit Prediction
# 3/3/19
# CTI-110 P2T1 - Sales Prediction
# Damien Cox
#
#Get the projected sales.
sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of projected sales.
profit = 0.23 * sales

#Display total profit.
print('The profit is $', format(profit, ',.2f'))
