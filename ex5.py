import random

#a) For loop applies for both.
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [i for i in range(1, 14)]


#b) Randomly generate integer lists of length 1-30-

a = [random.randint(0, 101) for i in range(random.randint(1, 31))]
b = [random.randint(0, 101) for i in range(random.randint(1, 31))]

c = []

#Generate a list with overlaps.
for i in a:
	for j in b:
		if j == i and j not in c:
			c.append(j)
			break

print("a: " + str(a))
print("b: " + str(b))

print("c: " + str(c))
