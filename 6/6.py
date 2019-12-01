def count_square_difference(natural_numbers):
	sum_of_squares = 0
	square_of_sum = 0
	sum = 0
	
	for number in range(natural_numbers + 1):
		sum = sum + number
		sum_of_squares = sum_of_squares + (number ** 2)
	
	square_of_sum = sum ** 2
	
	return square_of_sum - sum_of_squares
	

print(count_square_difference(100))
