# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
def sum():
    for x in range(2, 10):
        for y in range(2, x):
            if y % x == 0:
                return y 
    result = (x + y)

    return result


if __name__ == '__main__':
    result = sum()
    print(result)