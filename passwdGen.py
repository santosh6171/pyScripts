"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
use following link to learn more about string constants:
https://docs.python.org/3.1/library/string.html

"""


import random, string

def generate_passwd_strong():
    symbols = '!@#$%^&*'
# string.punctuation consists of ALL punctuation characters, includes all symbols
    allChar = (string.digits + string.ascii_letters + '!@#$%^&*')
    strongPass = "".join(random.sample(allChar,12))
#    print ("before check " +strongPass)
# usage of any function which would obtain a boolean output for all the iterations inside the loop and if any of it is true, it would return true, else false.
# usage of isdigit()/isalpha() functions for checking digit, alphabets 
    if any(char.isdigit() for char in strongPass):
#        print ("digitcheck")
        if any(char.isalpha() for char in strongPass):
#            print ("alphacheck")
            if any(c in symbols for c in strongPass):
#                print ("symbolcheck")
#                print (strongPass)
                return strongPass
            
    print ("looping again")
    return generate_passwd_strong()        
        
def generate_passwd_weak():
    weak = ['12345', '99999','123','abc']
    weak1 = random.sample(weak,1)
    return "".join(weak1)
#random.sample, provides an output in the form of a list
# usage of random.choice(list) provides a string output directly instead of using sample and then converting it.
    
#defmain():
if __name__ == '__main__':
    choice = int(input("Please enter 1 if you would like a strong passoword or 2 for a weak password\n"))
    if choice == 1:
        strongPwd = generate_passwd_strong()
#        print (strongPwd)
        print ("Your password that has been generated is " +strongPwd)
    elif choice == 2:
        weakPass = generate_passwd_weak()
        print ("Your password that has been generated is {0}" .format(weakPass))
    else:
        print ("Incorrect option entered, please try running the program again")
        
#main()
