def count_sum_of_digits():
	value = 2**1000
	sum = 0
	
	for number_char in str(value):
		sum += int(number_char)
		
	return sum

print(count_sum_of_digits())
