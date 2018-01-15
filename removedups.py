import random
import numpy as np

def get_set(x):
    return set(x)

def get_list(y):
        list2 = []
        [ list2.append(element) for element in y if element not in list2 ]
        return list2

    
 
list1 = input("Enter a list\n").split( )
listrand = np.random.choice(10,10,replace=True)
print (listrand)

newSet = get_set(list1)
print ("List with unique elements with sets function: {0}".format(newSet))
newList = get_list(list1)
print ("List with unique elements with loop iteration function: {0}".format(newList))









