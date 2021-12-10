Score = {
	")" : 3,
	"]" : 57,
	"}" : 1197,
	">"	: 25137
}

NumberOpen = {
	"(" : 0,
	"[" : 0,
	"{" : 0,
	"<" : 0, 
	")" : 0,
	"]" : 0,
	"}" : 0,
	">"	: 0
}

Pairs = {
	"(" : ")",
	"[" : "]",
	"{" : "}",
	"<" : ">",
}

def main():
	
	Points = 0

	with open("input.txt") as file:
		TabledInput = [x.strip() for x in file]

	
	for i in range(0, len(TabledInput)):
		NumberOpenRow = NumberOpen.copy()
		for _, InputChar in enumerate(TabledInput[i]):
			
			for _, Char in enumerate(NumberOpen):
				if InputChar == Char:
					NumberOpenRow[Char] += 1

if __name__ == "__main__":
	main()