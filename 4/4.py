palindromes = []

def is_palindrome(number):
	return str(number) == str(number)[::-1]
	
for x in range(100, 1000):
	for y in range(100, 1000):
		if is_palindrome(x * y):
			palindromes.append(x * y)
			
print(max(palindromes))
