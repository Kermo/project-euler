with open("11_input.txt") as f:
	lines = f.readlines()

grid = []

for line in lines:
	grid.append([int(i) for i in line.split()])
	
def count_largest_sum():
	largest = 0
	
	for x in range(20):
		for y in range(20):
			
			if y <= 16:
				horizontal = 1
				for z in range(4):
					horizontal *= grid[x][y + z]
				
				if horizontal > largest:
					largest = horizontal
			
			if y <= 16 and x <= 16:
				diagonal = 1
				for z in range(4):
					diagonal *= grid[x + z][y + z]
					
				if diagonal > largest:
					largest = diagonal
			
			
			if x <= 16:
				vertical = 1
				for z in range(4):
					vertical *= grid[x + z][y]
				
				if vertical > largest:
					largest = vertical
					
			if x >=3 and y <= 16:
				up_diagonal = 1
				for z in range(4):
					up_diagonal *= grid[x - z][y + z]
					
				if up_diagonal > largest:
					largest = up_diagonal
					
	return largest
	
print(count_largest_sum())			
			
