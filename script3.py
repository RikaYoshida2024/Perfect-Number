n = int(input())
if n<2:
    print(False)
elif n == 2:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    prime = True
    i=3
    while i*i <= n:
        if n % i == 0:
            prime = False
            break
        i += 2
    print(prime)
