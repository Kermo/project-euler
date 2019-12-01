with open("22_input.txt") as f:
	data = f.readline()


def count_points():
	names = data.split(",")
	names = sorted(names)
	points = 0
	
	for name in names:
		index = names.index(name)
		name = name.replace('"', '').strip()
		value = 0
		
		for char in name:
			value += (ord(char) - 64)
			
		points += (value * (index + 1))
	
	return points

	
print(count_points())		
