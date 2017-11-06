def long_string(input_list):
	result=len(input_list[0])
	for name1 in input_list:
		if len(name1)>len(result):
			result=name1
	return result
if __name__=='__main__':
	print(long_string(["sonam", "savita", "madhumita", "neha", "nikhitha", "shivangi", "keerthi", "banupriya"]))


	
