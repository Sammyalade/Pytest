import highest_element

def test_highest_element():
	list = [22, 12, 11, 19, 24, 78, 19]
	assert highest_element.highest_element(list) == 78
	elements = [1,2,3,4,5]
	assert highest_element.highest_element(elements) == 5