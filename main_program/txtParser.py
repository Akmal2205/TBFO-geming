import os

def txtParser(filename):
	global productions
	global total_states
	global word_symbols
	global stack_symbols
	global start_stack
	global start_symbol
	global acceptable_states
	global accept_with
	
	lines = [line.rstrip() for line in open(filename)]
	
	productions = []
	total_states = []
	word_symbols = []
	stack_symbols = []
	start_symbol = lines[3]
	start_stack = lines[4]
	acceptable_states = []
	accept_with = lines[6]
	
	total_states.extend(lines[0].split())
	word_symbols.extend(lines[1].split())
	stack_symbols.extend(lines[2].split())
	acceptable_states.extend(lines[5].split())
	i = 0
	temp=[]
	for line in lines:
		i += 1
		if (i > 7):
			prod = [item.strip() for item in line.split(' ')]
			temp.append(prod)
	for el in temp:
		if el[0] != '':
			productions.append(el)
	return productions