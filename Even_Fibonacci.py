def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1)+fib(n-2)

tot = 0
n = 0
while fib(n) <= 4000000:
    if fib(n) % 2 != 0:
        tot += fib(n)
    n += 1
print(tot)