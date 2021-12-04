import random

def CheckIfWon(Board, ChosenNumber, AllBoards, NumbersToChoose):

	ColumnNumberTrue = [0] * len(Board[0])

	for i in range(0, len(Board)):
		RowNumberTrue = 0
		for j in range(0, len(Board[i])):
			if Board[i][j] == True:
				RowNumberTrue += 1
				ColumnNumberTrue[j] += 1

		if RowNumberTrue == len(Board[0]):
			return CalculateScore(Board, ChosenNumber, AllBoards, NumbersToChoose)

	for k in range(0, len(ColumnNumberTrue)):
		if ColumnNumberTrue[k] == len(Board):
			return CalculateScore(Board, ChosenNumber, AllBoards, NumbersToChoose)

	return False, False

def MarkNumber(Board, ChosenNumber, AllBoards, NumbersToChoose):
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			if Board[i][j] == ChosenNumber:
				Board[i][j] = True
	_, r2 = CheckIfWon(Board, ChosenNumber, AllBoards, NumbersToChoose)
	if r2:
		return False, True

	return Board, False

def CalculateScore(Board, ChosenNumber, AllBoards, NumbersToChoose):
	Score = 0
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			if isinstance(Board[i][j], str):
				Score += int(Board[i][j])

	print(Score, " ", ChosenNumber, " ", Score * int(ChosenNumber))

	AllBoards.remove(Board)

	foo(AllBoards, NumbersToChoose)
	
	return True, True


def foo(AllBoards, NumbersToChoose):
	for i in range(0, len(NumbersToChoose)):
		for j in range(0, len(AllBoards)):

			if j >= len(AllBoards) or i >= len(NumbersToChoose):
				return False

			AllBoards[j], Stop = MarkNumber(AllBoards[j], NumbersToChoose[i], AllBoards, NumbersToChoose[i:])

			if Stop:
				return False

	return False

def main():
	AllBoards = []
	with open("input.txt", "r") as file:
		TabledFile = [x for x in file]

	NumbersToChoose = [str(x).strip("\n") for x in TabledFile[0].split(",")]

	del TabledFile[0] # Remove the numbers to choose

	for i in range(0, len(TabledFile)):
		if TabledFile[i] == "\n":
			AllBoards.append([])
			continue
		
		AllBoards[::-1][0].append(TabledFile[i].split())
	
	foo(AllBoards, NumbersToChoose)
	

main()