def odd_num(lst): 
	odd_lst =[ ] 
	for i in lst: 
		if i%2!=0: 
			x = odd_lst.append(i) 
	y = min(odd_lst) 
	return y 
	 
print(odd_num([9,200,3,1,4,5,76,7,5,4,34,5,6,6])) 