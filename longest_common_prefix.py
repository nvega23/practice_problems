"""Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".
 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl". """

def longestCommonPrefix(strs: list[str]) -> str:
	output = ""
	for lists in range(len(strs[0])):
		for x in strs:
			if lists == len(x) or x[lists] != strs[0][lists]:
				return output
		output += strs[0][lists]

	return output


if __name__ == "__main__":
	print("Running common prefix test")
	assert longestCommonPrefix(["lo","fl","fr"]) == ""
	assert longestCommonPrefix(["bso","bos","brl"]) == "b"
	assert longestCommonPrefix(["fro","frs","frl"]) == "fr"
	assert longestCommonPrefix(["flo","flo","flo"]) ==  "flo"
	assert longestCommonPrefix(["flor","flor","flor"]) ==  "flor"
	print("test passed!")