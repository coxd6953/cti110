# This is a program that asks the user for
# the number of males and the number of females registered in a class.
# The program will display the percentage of males and females in the class.

# 9/23/18

# CTI-110 P2HW2 - Male Female Percentage 

# Damien Cox

dmales = input('Please enter the number of males in class. ')
dfemales = input('Please enter the number of females in class. ')
males = int(dmales)
females = int(dfemales)
dtotal = males + females
maverage = males / dtotal
faverage = females / dtotal

# Display the data.
print ("\n" * 1)
print('Here is the data you entered:')
print('Males:', males)
print('Females:', females)
print ("\n" * 1)
print('Here are the averages:')
print('Males:', maverage, 'or', format(maverage, '.0%'),'percent')
print('Females:', faverage, 'or', format(faverage, '.0%'),'percent')
print ("\n" * 1)
