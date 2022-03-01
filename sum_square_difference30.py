# The sum of the squares of the first ten natural numbers is, 1² + 2² + 3²...+ 10² = 385

# The square of the sum of the first ten natural numbers is, (1+2+3...+10)²=55²= 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
def First_Ten():
    first = 0
    tots = 0
    res = 0
    for x in range(101):
        a = (x ** 2)
        first = first + a
        sp = (first)
    for x in range(101):
        tots = tots + x
        res = (tots ** 2)
        all = (res)
    print(all - sp)
if __name__ == '__main__':
    First_Ten() 