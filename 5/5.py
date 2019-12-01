def count_smallest_multiple(i):
	while(True):
		for x in range(1, 21):
			if i % x != 0:
				#print ("i: " + str(i) + ", break: " + str(x))
				break
			if (x == 20 and i % x == 0):
				return i
		i = i + 1
		
print(count_smallest_multiple(20))


# INTERESTING NOTE
# Finding primes from the range of (0-N) where N is the requested number and multiplying the primes always returns number which can be used
# to divide the smallest multiple
# example: finding the smallest multiple of number 1-10:
# primes are [1,3,5,7] and the multification returns 105
# This 105 can be used as steps for calculating the smallest multiple
# 105 * 24 = 2520, which is the smallest multiple of numbers 1-10

def is_prime(y):
	# print("is_prime: " + str(y))
	
	if y == 1:
		return True
	
	if y == 2:
		return False
	
	for z in range(2, y - 1):
		if y % z == 0:
			return False
	return True

def multiply_primes(init_number):
	value = 1
	primes = []
	
	for x in range(1, init_number+1):
		if is_prime(x):
			primes.append(x)
			
	#p rint("Primes: " + str(primes))
	for number in primes:
		value = value * number
		
	return value

def count_smallest_multiple_optimized(j):
	iteration_step = multiply_primes(j)
	
	potential_solution = 1
	multiplier = 1
	while(True):
		for x in range(1, j + 1):
			if (potential_solution % x) != 0:
				#print ("i: " + str(i) + ", break: " + str(x))
				break
			if (x == j and potential_solution % x == 0):
				return potential_solution
		multiplier = multiplier + 1
		potential_solution =  multiplier * iteration_step
		
print(count_smallest_multiple_optimized(20))
		
