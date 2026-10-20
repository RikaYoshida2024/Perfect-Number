n=int(input())
total=1
if n == 1:
    print(False)
else:
    i=2
    while i*i <= n:
        if n%i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    print(total == n)