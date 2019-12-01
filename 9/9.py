import math

def count_pythagorean_triplet():
	
	for a in range(1, 1000):
		for b in range(1, 1000):
			c = math.sqrt(a ** 2 + b ** 2)
			
			if (a + b + c == 1000):
				#print("Found: a: " + str(a) + ", b: " + str(b) + ", c: " + str(c))
				return a*b*c
				
print(count_pythagorean_triplet())
			
