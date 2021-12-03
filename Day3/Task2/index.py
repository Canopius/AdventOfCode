def Check(Item, ToRemove, i):
	if Item[i] != ToRemove:
		return True

	return False

def main():

	with open("input.txt", "r") as file:
		foo = [str(x).strip("\n") for x in file]

	
	Number0 = [0] * (len(foo[0])) # Stores the number of 0's in each column
	Number1 = [0] * (len(foo[0])) # Stores the number of 1's in each column

	OxygenFoo = foo.copy()
	CarbonFoo = foo.copy()
	
	for i in range(0, len(Number0)):
		if len(OxygenFoo) == 1:
			break

		Number0 = [0] * (len(OxygenFoo[0])) # Stores the number of 0's in each column
		Number1 = [0] * (len(OxygenFoo[0])) # Stores the number of 1's in each column

		for m in range(0, len(OxygenFoo)):
			for n in range(0, len(OxygenFoo[m])):
				if OxygenFoo[m][n] == "0":
					Number0[n] += 1
				elif OxygenFoo[m][n] == "1":
					Number1[n] += 1

		ToRemove = 0
		if Number0[i] > Number1[i]:
			ToRemove = "1"
		else:
			ToRemove = "0"

		OxygenFoo[:] = [Element for Element in OxygenFoo if Check(Element, ToRemove, i)]

	Oxygen = int("".join(OxygenFoo), 2)

	Number0 = [0] * (len(foo[0])) # Stores the number of 0's in each column
	Number1 = [0] * (len(foo[0])) # Stores the number of 1's in each column

	for i in range(0, len(Number0)):
		if len(CarbonFoo) == 1:
			break

		Number0 = [0] * (len(CarbonFoo[0])) # Stores the number of 0's in each column
		Number1 = [0] * (len(CarbonFoo[0])) # Stores the number of 1's in each column

		for m in range(0, len(CarbonFoo)):
			for n in range(0, len(CarbonFoo[m])):
				if CarbonFoo[m][n] == "0":
					Number0[n] += 1
				elif CarbonFoo[m][n] == "1":
					Number1[n] += 1

		ToRemove = 0
		if Number0[i] > Number1[i]:
			ToRemove = "0"
		else:
			ToRemove = "1"

		CarbonFoo[:] = [Element for Element in CarbonFoo if Check(Element, ToRemove, i)]

	Carbon = int("".join(CarbonFoo), 2)

	return Oxygen * Carbon

	

print(main())