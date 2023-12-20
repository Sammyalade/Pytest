def check_duplicate(values):
	store = 'No duplicates'
	length = len(values)
	for index in range(length):
		index2 = 0
		while index2 < length:
			if values[index2] == values[index]:
				store = values[index]
			index2 += 1
	return store

colors = ['blue', 'green', 'yellow', 'green', 'purple', 'purple']
print(check_duplicate(colors))