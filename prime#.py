def get_number():
    return int(input("Input a number\n"))

a = get_number()

if a == 0 or  a == 1:
        print ("Please enter a valid number, 1 or 0 is not a prime number\n")


x = [ i for i in range(a,1,-1) if a%i==0 ]

if len(x)>1:
    print ("This is not a prime number")
else:
    print ("This is a prime number")
