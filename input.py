#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime
name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
print ("Users Name is " +name +" and age is %d" %age)
remain = 100 - age
year = datetime.datetime.now().year
#year = datetime.date.today().year
x = year + remain
z = "You will turn 100 years old in the year: %d" %x
print ("Surprise me with a numberrrrrr ")
num = int(input())
i = 1
#while i <= num:
  # print ("You will turn 100 years old in the year: %d" %x)
  # i += 1

y = "test" * 5
print ("--------------------------------------------")
print ((z+"\n") * num)

   
