import random
a = random.sample(range(10),9)
b = random.sample(range(14),12)

print (a)
print (b)

c = [ i for i in a if i in b ]

print (c)
