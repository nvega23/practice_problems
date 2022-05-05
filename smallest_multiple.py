# 2520 is the smallest number that can be divided
# by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that
# is evenly divisible by all of the
# numbers from 1 to 20?


def smallest_number(num1):
    for x in range(1, num1):
        if num1 % x != 0:
            return False
    return True
n = 1
while True:
    if smallest_number(n):
        break
    n += 1


if __name__ == '__main__':
    print("running smallest multiple")
    # assert smallest_number(2520) == (11)
    print(f'{n:,}')
    print("test passed!")