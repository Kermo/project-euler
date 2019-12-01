def is_prime(number):
	
	#print("is_prime: " + str(number))
	
	if number == 1:
		return False
	if number == 2:
		return True
	
	for y in range(2, number - 1):
		if number % y == 0:
			return False
	
	return True

def find_nth_prime(nth):
	primes = []
	x = 1
	while True:
		if is_prime(x):
			primes.append(x)
			#print(str(primes))
		
		if len(primes) == nth:
			return primes[nth - 1]
		
		x = x + 1

print(find_nth_prime(10001))
