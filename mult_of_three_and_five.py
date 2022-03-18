# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def mults_three_five(num1):
    total = 0
    for x in range(num1):
        if (x % 3 == 0 or x % 5 == 0):
            total += x

    return total


if __name__ == "__main__":
    assert mults_three_five(1000) == 233168
    assert mults_three_five(1020) == 242250
    assert mults_three_five(1300) == 394118
    assert mults_three_five(1005) == 235170
    assert mults_three_five(10) == 23
    print("test passed!")