def popping_blocks(lst):
		def step(lst):
			if len(lst) == 2 and lst[0] == lst[1]:
					return []
			if len(lst) < 3:
					return lst
			idx = 0
			start = -1
			for idx, (prev, curr) in enumerate(zip(lst, lst[1:])):
					if start == -1 and prev == curr:
							start = idx
					if start != -1 and prev != curr:
							return lst[:start] + lst[idx+1:]
			if start == -1:
					return lst
			return lst[:start]
			
		current, last = step(lst), lst
		while current != last:
			current, last = step(current), current
		return current

if __name__ == '__main__':
	pop1 = popping_blocks(['A','B','B','A','C','A','B','B','A','C'])
	pop2 = popping_blocks(['C','C','A','B','B','C','A','B','B','A'])
	print(pop1)
	print(pop2)