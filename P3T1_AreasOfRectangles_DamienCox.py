# CTI-110
# P3T1 - Areas of Rectangles 
# Damien Cox
# 3/3/19

# Get area of rectangle one
len1 = int(input('What is the length of side one? '))
wid1 = int(input('What is the width of side one? '))
# Get area of rectangle two
len2 = int(input('What is the length of side two? '))
wid2 = int(input('What is the width of side two? '))

#calcate the area
area1 = len1 * wid1
area2 = len2 * wid2

# Display the data
if area1 > area2:
    print ("\n" * 1)
    print('Rectangle one has the greater area.')
    print ("\n" * 1)
elif area1 < area2:
    print ("\n" * 1)
    print('Rectangle two has the greater area.')
    print ("\n" * 1)
else :
    print ("\n" * 1)
    print('Both rectangles have the same area.')
    print ("\n" * 1)
