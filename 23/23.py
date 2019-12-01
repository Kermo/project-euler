from math import sqrt

def sum_dividers(number):
	sum = 0
	t = sqrt(number)
	
	for i in range(2, int(t) + 1):
		if number % i == 0:
			sum += i + number / i
		
	if int(t) == t:
		sum -= t
	
	return sum
			
def non_abundant_sum():
	
	abundants = set()
	sum = 0
	limit = 20162
	
	for x in range(1, limit):
		if sum_dividers(x) > x:
			abundants.add(x)
		
		if not any((x - a in abundants) for a in abundants):
			sum += x
	
	return sum


print(non_abundant_sum())
		
