fibonacci = [1,2]

sum = 0

while(True):
	next_value = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
	
	if (next_value <= 4000000):
		fibonacci.append(next_value)
	else:
		break
		
for number in fibonacci:
	if number % 2 == 0:
		sum = sum + number

print(sum)
