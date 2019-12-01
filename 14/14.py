def longest_sequence():
	
	step_array = []
	
	for x in range(1, 1000000):
		
		steps = 0
		value = x
		
		#print("x: " + str(value))
		while value > 1:
			
			if value % 2 == 0:
				value = value / 2
				#print("even, new value: " + str(value))
			else:
				value = 3 * value + 1
				#print("odd, new value: " + str(value))
		
			steps += 1
		
		#print("steps: " + str(steps))
		step_array.append(steps)
		#print(str(step_array))
		
	return str(step_array.index(max(step_array)) + 1)
	#return step_array

print(longest_sequence())
