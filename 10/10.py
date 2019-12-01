import math

number = 2000000

def is_prime(potential_prime):
	
	if potential_prime == 0:
		return False
	elif potential_prime == 1:
		return False
	else:
		
		for x in range(2, int(math.sqrt(potential_prime) + 1)):
			if potential_prime % x == 0:
				return False
		
		return True
		

def count_sum_of_primes(number):
	
	sum = 0
	
	primes = []
	for x in range(number):
		if is_prime(x):
			#print("prime: " + str(x))
			sum = sum + x
	
	return sum
	

print(count_sum_of_primes(number))
