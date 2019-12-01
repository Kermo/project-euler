lines = []
alt_pyramid = []

with open("18_input.txt") as f:
	lines = f.readlines()
	
def maximum_path():
	for line in lines:
		alt_pyramid.append(list(map(int, line.split(" "))))
	
	for i in range(len(alt_pyramid) - 1, 0, -1):
		next_line = alt_pyramid[i - 1]
		current_line = alt_pyramid[i]
		
		for j in range(len(next_line)):
			next_line[j] = max(next_line[j] + current_line[j], next_line[j] + current_line[j + 1])
			
	
	return alt_pyramid[0]
		
print(maximum_path())
