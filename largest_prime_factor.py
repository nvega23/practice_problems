"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
if not prime keep on dividing
"""
def factor(num1):
	output = []
	div = 2

	while div <= num1:
		if num1 % div == 0:
			output.append(div)
			num1 /= div
		div += 1

	return max(output)


if __name__ == "__main__":
	print("running largest prime factor...")
	assert factor(12) == 3
	assert factor(27) == 9
	assert factor(933) == 311
	assert factor(9317) == 121
	assert factor(13195) == 29
	assert factor(600851475143) == 6857
	print("test passed!")