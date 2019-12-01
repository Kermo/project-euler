import math

def find_triangular_number():
	
	i = 1
	factors = 0
	
	while factors < 500:
		factors = 0
		triangle = i * (i + 1) / 2
		
		for k in range(1, int(math.sqrt(triangle))):
			if (triangle % k == 0):
				factors += 1
			
		factors *= 2
		
		i += 1
	
	return triangle

print(find_triangular_number())
