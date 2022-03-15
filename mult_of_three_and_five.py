# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def mult(num1):
    total = 0
    for x in range(num1):
        if (x % 3 == 0 or x % 5 == 0):
            total += x

    return total


if __name__ == "__main__":
    total = mult(1000)
    print(total)
    assert mult(1000) == 233168
    assert mult(1020) == 242250
    assert mult(1300) == 394118
    assert mult(1005) == 235170
    assert mult(10) == 23
    print("test passed!")