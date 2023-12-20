def my_discount(price, discount):
	discount_allowed = int(discount * price / 100)
	amount_due = price - discount_allowed
	return amount_due
print(my_discount(1000, 10))