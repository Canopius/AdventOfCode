import random

def CheckIfWon(Board, ChosenNumber):

	ColumnNumberTrue = [0] * len(Board[0])

	for i in range(0, len(Board)):
		RowNumberTrue = 0
		for j in range(0, len(Board[i])):
			if Board[i][j] == True:
				RowNumberTrue += 1
				ColumnNumberTrue[j] += 1

		if RowNumberTrue == len(Board[0]):
			return CalculateScore(Board, ChosenNumber)

	for k in range(0, len(ColumnNumberTrue)):
		if ColumnNumberTrue[k] == len(Board):
			return CalculateScore(Board, ChosenNumber)


	return False

def MarkNumber(Board, ChosenNumber):
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			if Board[i][j] == ChosenNumber:
				Board[i][j] = True
	
	if CheckIfWon(Board, ChosenNumber):
		return False

	return Board

def CalculateScore(Board, ChosenNumber):
	Score = 0
	for i in range(0, len(Board)):
		for j in range(0, len(Board[i])):
			if isinstance(Board[i][j], str):
				Score += int(Board[i][j])

	print(Score, " ", ChosenNumber, " ", Score * int(ChosenNumber))
	exit()


def main():
	NumbersToChoose, AllBoards = [], []

	with open("input.txt", "r") as file:
		TabledFile = [x for x in file]
	
	NumbersToChoose = [str(x).strip("\n") for x in TabledFile[0].split(",")]

	del TabledFile[0] # Remove the numbers to choose

	for i in range(0, len(TabledFile)):
		if TabledFile[i] == "\n":
			AllBoards.append([])
			continue
		
		AllBoards[::-1][0].append(TabledFile[i].split())

	for i in range(0, len(NumbersToChoose)):
		for j in range(0, len(AllBoards)):
			AllBoards[j] = MarkNumber(AllBoards[j], NumbersToChoose[i])

	return False

main()