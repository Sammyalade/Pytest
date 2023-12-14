def highest(number1, number2, number3):
	
	highest_number = number1
	if number2 > highest_number:
		highest_number = number2
	if number3 > highest_number:
		highest_number = number3
	return highest_number

print(highest(7, 9, 2))
print(highest(2, 4, 10))
print(highest(15, 25, 10))