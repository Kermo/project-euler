def count_digits():
	
	mult = 1
	sum = 0
	
	for x in range(1, 101):
		mult *= x
	
	str_mult = str(mult)
	
	for num_char in str_mult:
		sum += int(num_char)
		
	return sum
	
print(count_digits())	
	
	
