import my_discount

def test_my_discount():
	assert my_discount.my_discount(2000, 15) == 1700
	assert my_discount.my_discount(10_000, 8) == 9200