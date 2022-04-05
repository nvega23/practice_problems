
def romanToInt(input_string: str) -> int:
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    output = 0
    last_char = None
    for char in input_string:
        value = roman[char]
        output += value
        if last_char:
            if last_char == "I" and char in ["V", "X"]:
                 output -= 2 
            if last_char == "X" and (char == "L" or char == "C"):
                 output -= 20 
            if last_char == "C" and (char == "D" or char == "M"):
                 output -= 200 
        last_char = char

    return output


if __name__ == "__main__":
    print("running tests for romanToInt...")
    assert romanToInt("I") == 1
    assert romanToInt("IV") == 4
    assert romanToInt("VI") == 6
    assert romanToInt("MCD") == 1400
    assert romanToInt("MCDLVI") == 1456
    assert romanToInt("MCMXCIV") == 1994
    print("test passed!")
