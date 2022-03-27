# "MCDLVI" == 1456
# "MCMXCIV" == 1994
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
    for char in input_string:
        value = roman[char]

        if input_string >= "IV":
            output = value - output

        elif input_string == "IX":
            output = value - output

        elif input_string == "XL":
            output = value - output

        elif input_string == "XC":
            output = value - output

        elif input_string == "CD":
            output = value - output
            continue
        elif input_string == "CM":
            output = value - output

        else:
            for char in input_string:
                value = roman[char]
                output += value
            return output
    return output


if __name__ == "__main__":
    assert romanToInt("IV") == 4
    assert romanToInt("CD") == 400
    assert romanToInt("MCD") == 1400
    assert romanToInt("MCMXCIV") == 1994
    print("test passed!")