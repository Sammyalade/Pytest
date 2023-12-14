def highest_element(elements):
	highest = 0
	for index in range(len(elements)):
		if elements[index] > highest:
			highest = elements[index]
		index += 1
	return highest

elements = [1, 2, 3, 4, 5]
list = [22, 12, 11, 19, 24, 78, 19]	
print(highest_element(elements))
print(highest_element(list))