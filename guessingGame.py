import random
num = random.randint(1,10)
#print (num)
guess = int(input("Please enter your guess\n"))
i=1
while guess != num:
    if guess > num:
        print ("Too high, try again!")
        i += 1
        guess = int(input("Please enter your guess again\n"))
        
    elif guess < num:
        print ("Too Low, try again!")
        i += 1
        guess = int(input("Please enter your guess again\n"))
        
print ("Your guess is exactly right!!\n")

print ("Total # of attempts: {0}\n" .format(i))
