""" Given a string s containing just the characters
'(', ')', '{', '}', '['and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order. """


def isValid(strings: str) -> bool:
    output = []
    braces = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    for symbols in strings:
        if symbols in braces:
            if output and output[-1] == braces[symbols]:
                output.pop()
            else:
                return False
        else:
            output.append(symbols)

    return True if not output else False


if __name__ == "__main__":
    print("running tests for valid parentheses")
    assert isValid("[") == False
    assert isValid("(") == False
    assert isValid("()") == True
    assert isValid("([])") == True
    assert isValid(")(") == False
    assert isValid("[)") == False
    print("Test passed!")
