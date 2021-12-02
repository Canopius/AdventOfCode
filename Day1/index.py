def main():

	Prev = False
	Counter = 0
	Sum = []

	with open("input.txt", "r") as file:
		foo = [int(x) for x in file]

	for i in range(0, len(foo)-2):
		Sum.append(foo[i] + foo[i+1] + foo[i+2])

	
	for i in range(0, len(Sum)):

		if Prev == False:
			Prev = Sum[i]

		if Sum[i] > Prev:
			Counter += 1

		Prev = Sum[i]

	return Counter
	

print(main())