ones = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

tens = {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

hundred = "hundred"

thousand = "onethousand"

and_chars = "and"


def count_length():
	
	full_string = ""
	
	for number in range(1, 1001):
		number_string = str(number)
		
		number_length = len(number_string)
		
		if number_length == 1:
			full_string += ones.get(number)
			
		elif number_length == 2:
			
			if number in teens:
				full_string += teens.get(number)
			else:
				full_string += tens.get(int(number_string[0]))
				
				if int(number_string[1]) != 0:
					full_string += ones.get(int(number_string[1]))

		elif number_length == 3:
				
				full_string += ones.get(int(number_string[0]))
				full_string += hundred
				
				if (int(number_string[1]) or int(number_string[2])) != 0:
					full_string += and_chars
				
				if int(number_string[1]) != 0:
					
					if int(number_string[1:]) in teens:
						full_string += teens.get(int(number_string[1:]))
					else:						
						full_string += tens.get(int(number_string[1]))
						
						if int(number_string[2]) != 0:
							full_string += ones.get(int(number_string[2]))
				
				else:
					if int(number_string[2]) != 0:
						full_string += ones.get(int(number_string[2]))
					
		else:
			full_string += thousand
			
	return len(full_string)

print(count_length())
