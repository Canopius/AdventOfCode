def main():
	with open("input.txt") as file:
		TabledInput = [x.split(" | ") for x in file]

	Total = 0

	for i in range(0, len(TabledInput)):
		TabledInput[i][0] = TabledInput[i][0].split(" ")
		TabledInput[i][1] = TabledInput[i][1].split(" ")

		for j in range(0, len(TabledInput[i][1])):
			Combination = TabledInput[i][1][j].strip()
			
			if len(Combination) == 2 or len(Combination) == 4 or len(Combination) == 3 or len(Combination) == 7:
				Total += 1

	return Total

if __name__ == "__main__":
	print(main())