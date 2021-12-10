def SortString(ToSort):
	AllLetters = [x for x in ToSort]
	AllLetters.sort()
	return "".join(AllLetters)

def main():
	with open("input.txt") as file:
		TabledInput = [x.split(" | ") for x in file]

	Total = 0

	for i in range(0, len(TabledInput)):
		TabledInput[i][0] = list(map(SortString, TabledInput[i][0].split(" ")))
		TabledInput[i][1] = list(map(SortString, TabledInput[i][1].split(" ")))

		"""
		0 -> 6
		1 -> 2 #
		2 -> 5
		3 -> 5
		4 -> 4 #
		5 -> 5
		6 -> 6
		7 -> 3 #
		8 -> 7 #
		9 -> 6
		"""

		for j in range(0, len(TabledInput[i][1])):
			Combination = TabledInput[i][1][j].strip()
			
			if len(Combination) == 2 or len(Combination) == 4 or len(Combination) == 3 or len(Combination) == 7:
				Total += 1

	return Total

if __name__ == "__main__":
	print(main())