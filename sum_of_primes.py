# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
def sum(num1, num2):
    for x in range(num1, num2):
        for y in range(20, x):
            if y % x == 0:
                return y
    result = (x + y)

    return result


if __name__ == '__main__':
    result = sum(1999999, 2000000)
    print(result)
    assert sum(1999999, 2000000) == 3999997