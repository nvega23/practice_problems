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
				output -= 2 
			if last_character == "X" and char in ["L", "C"]:
				output -= 20 
			if last_character == "C" and char in ["D", "M"]:
				output -= 200 
		last_character = char


	return output



if __name__ == "__main__":
	print("running romans to ints")
	assert romanToInt("I") == 1
	assert romanToInt("IV") == 4
	assert romanToInt("VI") == 6
	assert romanToInt("IX") == 9
	print("Test passed!")