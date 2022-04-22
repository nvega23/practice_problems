"""
Given a string s containing just the characters
'(', ')', '{', '}', '['and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def is_valid(strings: str) -> bool:
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

    return not output


if __name__ == "__main__":
    print("running tests for valid parentheses")
    assert is_valid("[") == False
    assert is_valid("(") == False
    assert is_valid("()") == True
    assert is_valid("([])") == True
    assert is_valid(")(") == False
    assert is_valid("[)") == False
    assert is_valid("((){})[]") == True
    print("Test passed!")