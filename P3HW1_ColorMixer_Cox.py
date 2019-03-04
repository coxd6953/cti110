# CTI-110 
# P3HW1 - Color Mixer 
# Damien Cox
# 3/3/19
#
#Enter the name of two primary colors.
print('Please choose a primary color of red, yellow or blue.')
color1 = input('Enter your first primary color.')
if color1 != 'red' or 'yellow' or 'blue':
    print("That isn't a PRIMARY color!")
    exit()
color2 = input('Enter your second primary color.')
if color2 != 'red' or 'yellow' or 'blue':
    print("That isn't a PRIMARY color!")
    exit()

#Mix the colors entered.
if color1 == 'red' and color2 == 'blue':
    print("Your secondary color is purple!")
elif color1 == "red" and color2 == "yellow":
    print("Your secondary color is orange!")
elif color1 == "blue" and color2 == "yellow":
    print("Your secondary color is green!")
