def duplicate_encode(word):
	l1 = list(word.lower())
	for index in range(len(l1)):		
		list_of_duplicates_for_item = [dup_index for dup_index, item in enumerate(l1) if item == l1[index] and l1.count(l1[index]) > 1]				
		for dup_index in list_of_duplicates_for_item: 
			l1[dup_index] = ')'

	for i in range(len(l1)):
		if l1.count(l1[i]) <= 1:
			if l1[i] == '@':
				l1[i] = '(('
			if l1[i] == '(':
				l1[i] = ')'
			if l1[i] != '@':
				l1[i] = '('


	word = ''.join(l1);
	return word


