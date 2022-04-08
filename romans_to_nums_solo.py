""" Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. """


def romanToInt(input_string: str) -> int:
	romans = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}
	last_character = None
	output = 0
	for char in input_string:
		value = romans[char]
		output += value
		if last_character:
			if last_character == "I" and char in ["V", "X"]:
				output -= 2 * romans["I"]
			if last_character == "X" and char in ["L", "C"]:
				output -= 2 * romans["X"]
			if last_character == "C" and char in ["D", "M"]:
				output -= 2 * romans["C"]
		last_character = char

	return output


if __name__ == "__main__":
	print("running romans to ints")
	assert romanToInt("I") == 1
	assert romanToInt("IV") == 4
	assert romanToInt("VI") == 6
	assert romanToInt("IX") == 9
	assert romanToInt("MCDLVI") == 1456
	assert romanToInt("MCMXCIV") == 1994
	print("Test passed!")