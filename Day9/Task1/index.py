def main():
	with open("input.txt") as file:
		TabledInput = [x.strip() for x in file]

	Total = 0

	for y in range(0, len(TabledInput)):
		for x in range(0, len(TabledInput[y])):

			Up = 0
			Down = 0
			Left = 0 
			Right = 0

			if not len(TabledInput[y]) > x + 1:
				# Right
				Right = 999
				Left = int(TabledInput[y][x-1]) # <-- Left
			elif x == 0:
				# Left
				Left = 999
				Right = int(TabledInput[y][x + 1]) # <-- Right
			else:
				Left = int(TabledInput[y][x-1]) # <-- Left
				Right = int(TabledInput[y][x + 1]) # <-- Right

			if not len(TabledInput) > y + 1:
				# Bottom
				Down = 999
				Up = int(TabledInput[y - 1][x])
			elif y == 0:
				# Top
				Up = 999
				Down = int(TabledInput[y + 1][x])
			else:
				Up = int(TabledInput[y - 1][x])
				Down = int(TabledInput[y + 1][x])

			Current = int(TabledInput[y][x])
			
			if Current < Left and Current < Right and Current < Up and Current < Down:
				Total += (Current + 1)
		
	return Total

if __name__ == "__main__":
	print(main())