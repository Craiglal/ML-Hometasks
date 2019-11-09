def funcA(first_val, second_val, div_val=4):
    result = (first_val*2) - (second_val/div_val)
    return result

def functionB(first_val=23, last_val=72):
	breakpoint()
	response = funcA(first_val, last_val, div_val=0)
	result = response * first_val / 7
	return result
    
functionB(33,88) # we are evaluating the funciton.