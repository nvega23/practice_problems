# The sum of the squares of the first ten natural numbers is,
# 1² + 2² + 3²...+ 10² = 385

# The square of the sum of the first ten natural numbers is,
# (1+2+3...+10)²=55²= 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum


def first_ten():
    first = 0
    tots = 0
    res = 0

    # the first for loop will gather the 1² + 2² + 3²...+ 10² = 385 or wichever
    # number is wanted
    for x in range(101):
        first += x ** 2
        sums = (first)

    # this second for loop will gather the (1+2+3...+10)²=55²= 3025 or any
    # other number and subtract from the two loops
    for x in range(101):
        tots += x
        res = (tots ** 2)
        result = (res - sums)

    return result

<<<<<<< HEAD

if __name__ == '__main__':
    result = first_ten()
    print(result)
=======
        all = (res - sums)
    return all

if __name__ == '__main__':
    all = first_ten()
    print(all)

    
>>>>>>> 555901b (placed a return call in main)
