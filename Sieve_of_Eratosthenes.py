def seive(n):
    print(n)
    prime = [True for i in range(n + 1)] # Assigning every (n)->numbers as True and assuming every number as a prime
    print(prime)
    p = 2                               # intializing start point as 2
    while p * p <= n:                   # Checking p * p is less than or equal to (n) i.e --> given number
        if prime[p] == True:            # If we found p as true in prime list/arrey and then next line will be executed
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p = p + 1

    for j in range(2, n):
        if prime[j]:
            print(j)

seive(50)


