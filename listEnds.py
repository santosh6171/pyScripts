def get_list():
#    listofnum = input("Provide a list of numbers\n").split( )
    return [ int(x) for x in input("Provide a list of numbers\n").split() ]

def get_ends():
    return [ listofnum[0], listofnum[-1] ]

listofnum = get_list()
listofends = get_ends()
print (listofends)
