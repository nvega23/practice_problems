"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143? 
"""
def is_prime(n):
	if n <= 2:
		return False
	for x in range(2, num1):
		if x ** 2 > n:
			break
		if n % x == 0:
			return False
	return True

def factors(num1):
	output = ()
	if is_prime == False:
		for x in range(2, num1):
			if x % num1 == 0:
				output += x
		return output


if __name__ == "__main__":
	output = factors(10)
	print(output)