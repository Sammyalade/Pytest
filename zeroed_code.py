def zeroed_code(values):
	last_index = len(values) - 1
	values[0] = 0
	values[last_index] = 0
	return values
numbers = [1,2,3,4,5]
print(zeroed_code(numbers))