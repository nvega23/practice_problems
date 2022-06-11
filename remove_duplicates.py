def remove_duplicates_with_sets(num):
	return len(list(set(num))), list(set(num))

if __name__ == '__main__':
	print("running remove_duplicates_with_sets...")
	assert remove_duplicates_with_sets([1,2,3,3,4,5,5,5]) == (5, [1,2,3,4,5])
	assert remove_duplicates_with_sets([1,1,1,2]) == (2, [1, 2])
	assert remove_duplicates_with_sets([0,0,1,1,1,2,2,3,3,4]) == (5, [0,1,2,3,4])
	assert remove_duplicates_with_sets([1,2,3,3,4,5]) == (5, [1, 2, 3, 4, 5])
	print("test passed!")


	# this code below runs on leetcode but does
	# not run the same on sublime

	# leetcode = [1,1,2]
	# output_leetcode = [1,2]

	# sublime = [1,1,2]
	# output_sublime = [3]
def remove_duplicate_in_place(nums):
	unique_value = 1

	for number in range(1, len(nums)):

	# check if number has been seen and if not then its a
	# unique_value
		if nums[number] != nums[number - 1]:

	# if number is a unique_value then we can put it in our
	# unique_value variable
			nums[unique_value] = nums[number]
			unique_value += 1

	return unique_value


if __name__ == '__main__':
	print("running remove_duplicate_in_place...")
	assert remove_duplicate_in_place([1, 1, 2]) == 2
	assert remove_duplicate_in_place([0, 1, 1, 2]) == 3
	assert remove_duplicate_in_place([1, 2]) == 2
	assert remove_duplicate_in_place([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
	print("test passed!")


def remove_duplicates_output(num):
	output = []

	for number in range(len(num)):
		if num[number] != num[number -1]:
			output.append(num[number])

	return len(output), output


if __name__ == '__main__':
	print("running remove_duplicates_output...")
	assert remove_duplicates_output([1,2,3,3,4,5,5,5]) == (5, [1,2,3,4,5])
	assert remove_duplicates_output([1,1,1,2]) == (2, [1, 2])
	assert remove_duplicates_output([0,0,1,1,1,2,2,3,3,4]) == (5, [0,1,2,3,4])
	assert remove_duplicates_output([1,2,3,3,4,5]) == (5, [1, 2, 3, 4, 5])
	print("test passed!")