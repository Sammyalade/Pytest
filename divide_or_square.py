def divide_or_square(input):
	modulus = input % 5
	square_root = 0
	display = 0
	if modulus == 0:
		square_root = input ** 0.5
		display = square_root
	elif modulus != 0:
		display = modulus
	return display

print(divide_or_square(10))
print(divide_or_square(7))
		
	