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
		else:
			div += 1

	return output


if __name__ == "__main__":
	print("running largest prime factor...")
	assert factor(12) == [2, 2, 3]
	assert factor(27) == [3, 3, 3]
	assert factor(933) == [3, 311]
	assert factor(9317) == [7, 11, 11, 11]
	assert factor(13195) == [5, 7, 13, 29]
	assert factor(600851475143) == [71, 839, 1471, 6857]
	print("test passed!")