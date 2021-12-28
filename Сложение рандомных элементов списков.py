from random import randint

def sum_lists(value, min, max):
	a = []
	b = []
	x = 0
	while x < value:
		a.append(randint(min,max))
		b.append(randint(min,max))
		x += 1			
	c = list(map(sum, zip(a,b)))
	numb_c = len(c)
	print("list first:", a)
	print("list second:", b)
	print("Sum of a, b:", c)
	print("Amount of elements of lists a and b:", numb_c)
	return

x=int(input('value of lists: '))
y=int(input('min rand: '))
z=int(input('max rand: '))

sum_lists(value = x, min = y, max = z)
