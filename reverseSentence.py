
def get_reverse_string(str):
     liststr = str.split()
     return " ".join(liststr[::-1])

string = input("Enter a sentence to be reversed\n")
reverseString = get_reverse_string(string)
print ("Reversed string is: {0}" .format(reverseString))
