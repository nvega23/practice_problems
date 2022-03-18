# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
def is_primes(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if x ** 2 > n:
            break
        if n % x == 0:
            return False
    return True


def sum(num1):
    result = 0
    for x in range(num1 + 1):
        if is_primes(x):
            result += x
    return result

if __name__ == "__main__":
    assert sum(5) == 10
    assert sum(17) == 58
    assert sum(224) == 4661
    assert sum(2000000) == 142913828922
    print("test passed!")