# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10,001st prime number?

def prime_number(div):
    num1 = 2
    count = 0
    prime = 0
    now = []
    while count < div:
        for x in range (2, num1 + 1):
            if len(now) == 2:
                break
            elif num1 % x == 0:
                now.append(x)

        if len(now) == 1:
            prime = num1
            count += 1
        now = []
        num1 += 1

    return prime


if __name__ == '__main__':
    assert prime_number(1) == 2
    assert prime_number(6) == 13
    assert prime_number(11) == 31
    assert prime_number(102) == 557
    print("Test passed!")