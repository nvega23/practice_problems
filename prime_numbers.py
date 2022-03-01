# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?
div = 10001
i = 2
count = 0
prime = 0
now = []

while count < div:

    for x in range (2,i + 1):
        if len(now) == 2:
            break
        elif i % x == 0:
            now.append(x)

    if len(now)==1:
        prime = i
        count += 1
    now = []
    i += 1



print(prime)
