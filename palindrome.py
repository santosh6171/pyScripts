wrd=input("Please enter a word\n")
wrd=str(wrd)
if wrd[::1]==wrd[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
