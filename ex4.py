numb = int(input("Enter #: "))

#a)
#a = []

#for i in range(1, numb + 1):
#	if numb % i == 0:
#		a.append(i)

#print(a)

#Alternative 
b = [i for i in range(1, numb +1) if numb % i == 0]

print(b)
