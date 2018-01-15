a = input("Enter few random numbers with space separator\n").split()
b = input("Enter few random numbers with space separator for 2nd list\n").split()
c = []
for i in a:
    if i in b and i not in c:
             c.append(i)
print (c)
