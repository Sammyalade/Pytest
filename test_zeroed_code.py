import zeroed_code

def test_zeroed_code():
	numbers = [9,3,4,2,7]
	number2 = [0,3,4,2,0]
	assert zeroed_code.zeroed_code(numbers) == number2