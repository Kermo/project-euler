def sum_of_dividers(number):
	dividers = []
	
	for a in range(1, number):
		if number % a == 0:
			dividers.append(a)
	return sum(dividers)
		
def count_amicables_sum():
	
	amicables = []
	
	for x in range(1, 10000):
		
		sum_dividers = sum_of_dividers(x)
		
		if (sum_of_dividers(sum_dividers) == x and sum_dividers != x):
			if x not in amicables:
				amicables.append(x)
			if sum_dividers not in amicables:
				amicables.append(sum_dividers)
	
	return sum(amicables)
	
print(count_amicables_sum())
		
