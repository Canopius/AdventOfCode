def triangularNumber(n):
    return n * (n + 1) // 2

def main():

	with open("input.txt", "r") as file:
		Input = [x.strip().split(",") for x in file]

	Input = list(map(int, Input[0]))
	Input.sort()

	PossibleSolutions = []

	for i in range(Input[0], Input[-1] + 1):
		Total = 0
		for j in range(0, len(Input)):
			Total += triangularNumber(abs(i - Input[j]))

		PossibleSolutions.append(Total)

	PossibleSolutions.sort()

	return PossibleSolutions[0]

if __name__ == "__main__":
	print(main())