def main():

	Horizontal = 0
	Aim = 0
	Vertical = 0

	with open("input.txt", "r") as file:
		foo = [x.split() for x in file]


	for i in range(0, len(foo)):
		if foo[i][0] == "forward":
			Horizontal += int(foo[i][1])
			Vertical += Aim * int(foo[i][1])
		elif foo[i][0] == "up":
			Aim -= int(foo[i][1])
		else:
			Aim += int(foo[i][1])

	return Horizontal * Vertical

print(main())