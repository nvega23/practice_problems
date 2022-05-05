"""
Given a string s consisting of some words separated
by some number of spaces, return the length of the
last word in the string.

A word is a maximal substring consisting of
non-space characters only.
"""
def last_word(word):
	output = word.split()
	return len(output[-1])

if __name__ == '__main__':
	print("running tests for last word length...")
	assert last_word("hey there bud") == 3
	assert last_word("One piece is the best anime") == 5
	assert last_word("Another practice_problem") == 16
	print("Test passed!")