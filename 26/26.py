def find_longest_cycle():
	num = longest = 1
	for x in range(3, 1000, 2):
		
		if x % 5 == 0:
			continue
			
		cycle = 1
		
		while (10 ** cycle) % x != 1:
			cycle += 1
		
		if cycle > longest:
			num, longest = x, cycle
		
	return num
			
print(str(find_longest_cycle()))
