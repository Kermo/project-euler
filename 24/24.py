from itertools import	permutations

numbers = "0123456789"

def count_permutations():
	perms = []
	for p in permutations(numbers):
		perms.append(p)
		
		if len(perms) == 1000000:
			return perms[999999]
	
print(count_permutations())
		
