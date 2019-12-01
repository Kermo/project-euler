with open("13_input.txt") as f:
	lines = f.readlines()
	
def return_10_digits():

	sum = 0
	
	for line in lines:
		sum += int(line)
		
	splitted_sum = str(sum)[0:10]
	
	return(splitted_sum)

print(return_10_digits())
