def main():

	with open("input.txt", "r") as file:
		foo = [str(x) for x in file]
	
	Number0 = [0] * (len(foo[0]) - 1) # Stores the number of 0's in each column
	GammaRate = [0] * (len(foo[0]) - 1) 
	EpsilonRate = [0] * (len(foo[0]) - 1)

	TotalLines = len(foo)

	for i in range(0, TotalLines):
		for j in range(0, len(foo[i])):
			if foo[i][j] == "0":
				Number0[j] += 1

	for i in range(0, len(Number0)):
		if Number0[i] > (TotalLines / 2):
			GammaRate[i] = "0"
			EpsilonRate[i] = "1"
		else:
			GammaRate[i] = "1"
			EpsilonRate[i] = "0"

	

	return int("".join(GammaRate), 2) * int("".join(EpsilonRate), 2)

	

print(main())