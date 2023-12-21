import check_duplicate

def test_check_duplicate():
	numbers = [1, 2, 3, 2, 5, 7, 1]
	numbers2 = [1, 2, 3, 4, 5, 6]
	assert check_duplicate.check_duplicate(numbers) == 2
	assert check_duplicate.check_duplicate(numbers2) == 'No duplicates'