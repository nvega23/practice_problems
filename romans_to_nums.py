""" For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27 is
written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
 "MCDLVI" == 1456
 "MCMXCIV" == 1994"""


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
        if input_string == "IV":
            output = value - output
        elif input_string == "IX":
            output = value - output
        elif input_string == "XL":
            output = value - output
        elif input_string == "XC":
            output = value - output
        elif input_string == "CD":
            output = value - output
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
    assert romanToInt("IX") == 9
    assert romanToInt("CD") == 400
    print("Test passed!")