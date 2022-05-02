# Two strings are anagrams if they're made of
# the same characters with the same frequences.

def anagram(s1,s2):
	# checks if both strings are the same length.
	if len(s1) != len(s2):
		return False

	freq1 = {}
	freq2 = {}

	for char in s1:
		if char in freq1:
			freq1[char] += 1
		else:
			freq1[char] = 1

	for chars in s2:
		if chars in freq2:
			freq2[chars] += 1
		else:
			freq2[chars] = 1

	for key in freq1:
		if key not in freq2 or freq1[key] != freq2[key]:
			return False
	return True


if __name__ == '__main__':
	print("running anagram tests...")
	assert anagram("nameless","salesmen") == True
	assert anagram("codes","coast") == False
	assert anagram("debitcard","badcredit") == True
	assert anagram("apple","snapple") == False
	assert anagram("schoolmaster","theclassroom") == True
	print("test passed!")