def Counter(Arr):
	Result = {}

	for item in Arr:
		if item not in Result:
			Result[item] = 1
		else:
			Result[item] +=1

	return Result

def main():
	with open("input.txt", "r") as file:
		TabledFile = [x.strip().split(" -> ") for x in file]

	AllCoords = []

	for _, Content in enumerate(TabledFile):
		Content = [x.split(",") for x in Content]

		if Content[0][0] == Content[1][0]:
			# X Same
			Small = min(int(Content[0][1]), int(Content[1][1]))
			Big = max(int(Content[0][1]), int(Content[1][1]))
			for Number in range(Small, Big + 1):
				AllCoords.append(Content[0][0] + "," + str(Number))

		elif Content[0][1] == Content[1][1]:
			# Y Same
			Small = min(int(Content[0][0]), int(Content[1][0]))
			Big = max(int(Content[0][0]), int(Content[1][0]))
			for Number in range(Small, Big + 1):
				AllCoords.append(str(Number) + "," + Content[0][1])


	NumberRecourances = Counter(AllCoords)
	Total = 0

	for i in NumberRecourances:
		if NumberRecourances[i] > 1:
			Total += 1

	return Total

print(main())