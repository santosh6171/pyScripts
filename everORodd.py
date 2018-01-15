#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#Extras:
#    If the number is a multiple of 4, print out a different message.
#    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Enter a number that you fantasize about ...lol\n"))

check = int(input("Enter another one plzzz \n"))

if num%check == 0:
    print ("The number {0} divides evenly with {1}" .format(num,check))
    exit()

if num%2 == 1:
    print ("The number {0} is an odd number" .format(num))
else:
    if num%4 == 0:
        print ("The number {0} is a multiple of 4!!!" .format(num))
    else:
        print ("The number {0} is an even number" .format(num))


