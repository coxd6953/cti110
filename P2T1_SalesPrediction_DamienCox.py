# A company has determined that its annual profit is
# typically 23 percent of total sales.
# This is a program that asks the user to enter
# the projected amount of total sales, and then
# displays the profit that will be made from that amount

# 9/23/18

# CTI-110 P2T1 - Sales Prediction

# Damien Cox

# Get the total amount of projected sales and then calculate the profit.
dsales = input('What is the total amount of projected sales? ')
psales = int(dsales)
profit = .23 * (psales)

# Display the data.
print ("\n" * 1)
print('Here is the data you entered:')
print('Projected Sales:', psales)
print('Profit:', profit)
print ("\n" * 1)
