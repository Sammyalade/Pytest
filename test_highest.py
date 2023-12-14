import highest

def test_highest():
	assert highest.highest(7, 9, 5) == 9
	assert highest.highest(6, 9, 14) == 14
	assert highest.highest(55, 2, 3) == 55