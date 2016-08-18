def super_sum(*var_list):
	total = 0
	for i in var_list:
		if isinstance(i, list):
			for item in i:
				total += item

		elif isinstance(i, int):
			total += i

		elif isinstance(i, float):
			total += i

		

	return total

#print super_sum([10,5],5.5)	

			
