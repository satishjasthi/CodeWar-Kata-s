
def duplicate_encoder(word):
	l1 = list('recede') # converting string to list of individual characters
	for index in range(len(l1)): #gathering and replacing the indexes of repeated elements of the list		
		list_of_duplicates_for_item = [dup_index for dup_index, item in enumerate(l1) if item == l1[index] and l1.count(l1[index]) > 1]				
		for dup_index in list_of_duplicates_for_item: 
			l1[dup_index] = ')'

	for i in range(len(l1)):#gathering and replacing the indexes of non-repeated elements of the list
		if l1.count(l1[i]) <= 1:
			l1[i] = '('


	word = ''.join(l1);#joining the list of elements from list into a string
	return word


