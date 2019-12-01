def count_fibonacci_digits():
	
	fibonacci = {"1":"1", "2":"1"}
	index = 2
	
	while len(fibonacci[str(index)]) < 1000:
		index += 1
		next_value = int(fibonacci[str(index - 1)]) + int(fibonacci[str(index - 2)])
		fibonacci[str(index)] = str(next_value)
		del fibonacci[str(index - 2)]

	return index
		 	
print(count_fibonacci_digits())
