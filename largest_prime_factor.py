"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143? 
if not prime keep on dividing
"""
def factor(x):
	prime_factor = []
	div = 2
	while div <= x:
		if x % div == 0:
			prime_factor.append(div)
			x = x / div
		else:
			div += 1
	return prime_factor


if __name__ == "__main__":
	print("running largest prime factor...")
	assert factor(15) == [3, 5]
	assert factor(159) == [3, 53]
	assert factor(12345) == [3, 5, 823]
	assert factor(13195) == [5,7,13,29]
	assert factor(600851475143) == [71, 839, 1471, 6857]
	print("test passed!")