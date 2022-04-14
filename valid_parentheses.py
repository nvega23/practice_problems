"""
Given a string s containing just the characters
'(', ')', '{', '}', '['and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def isValid(strings: str) -> bool:
    output = []
    braces = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for char in strings:
        if char in braces:
            if output and output[-1] == braces[char]:
                output.pop()
            else:
                return False
        else:
            output.append(char)

    return True if not output else False


if __name__ == "__main__":
    print("running tests for valid parentheses")
    assert isValid("[") == False
    assert isValid("(") == False
    assert isValid("()") == True
    assert isValid("([])") == True
    assert isValid(")(") == False
    assert isValid("[)") == False
    assert isValid("((){})[]") == True
    print("Test passed!")
