def main():
	TabledInput = []

	with open("input.txt", "r") as file:
		TabledInput = [int(x) for x in file]

	return TabledInput
	
if __name__ == "__main__":
	print(main())