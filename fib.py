def fib(count):
    if count<2:
        return count
    else:
        return (fib(count-1) + fib(count-2))

n = int(input("Please enter a number to generate fibonacci series for\n"))
fibbs = []
while n>=1:
    fibbs.append(fib(n))
    n-=1
    
print (fibbs[::-1])
