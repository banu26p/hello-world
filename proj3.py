def find_longer_than_n(input_list, length):
    list_output=[]
	for name1 in input_list:
		if len(name1)>length:
			list_output.append(name1)
	return list_output
if __name__=='__main__':
	for name1 in (find_longer_than_n(["sonam", "savita", "madhumita", "neha", "nikhitha", "shivangi", "keerthi", "banupriya"],4)):
		print name1

	
