def only_float(a, b):
	count = 0
	type_a = float.is_integer(a)
	type_b = float.is_integer(b)
	if type_b == False:
		count += 1
	if type_a == False:
		count += 1
	return count

print(only_float(1.5, 1.3))