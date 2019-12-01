def find_longest_cycle():
	cycle = []
	for x in range(2, 1000):
		threshold = 1000
		left = 10
		while(threshold > 0):
			left = left % x
			cycle.append(left)
			
			print(cycle)
			
			if left == 0:
				break
			
			left = left * 10
			
			threshold =- 1
		
	return len(cycle)
			
print(str(find_longest_cycle()))

