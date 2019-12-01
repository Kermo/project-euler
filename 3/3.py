import math

number = 600851475143
primes = []

def is_prime_factor(x):
	if number % x == 0:
		for y in range(2, x - 1):
			if x % y == 0:
				return False
		return True
	else:
		return False
		
for x in range(1, math.floor(number ** 0.5)):
	if (is_prime_factor(x)):
		primes.append(x)
				
print(max(primes))
