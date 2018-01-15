
# create a list with even numbers from a list
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = input("Enter the input list\n").split( )
print ([i for i in a if int(i) % 2 == 0 ])
