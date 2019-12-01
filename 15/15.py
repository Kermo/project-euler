row = 21
col = 21

paths = [[0 for x in range(row)] for y in range(col)]

def count_lattice_paths():
	for i in range(row):	
		for j in range(col):
			if (i == 0 or j == 0):
				paths[i][j] = 1
			else:
				paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
	print(paths)			
	return paths[row - 1][col - 1]

print(count_lattice_paths())
