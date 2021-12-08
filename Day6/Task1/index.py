Days = 80
FishObjects = []

class LanternFish:
	def __init__(self, _counter):
		self.Counter = _counter

	def Age(self):
		self.Counter -= 1

		if self.Counter < 0:
			self.Counter = 6
			NewFish = LanternFish(8)
			FishObjects.append(NewFish)
			

def Main():

	TabledFile = []

	with open("input.txt", "r") as file:
		TabledFile = [x.strip().split(",") for x in file]

	InitialFish = TabledFile[0]

	for _, counter in enumerate(InitialFish):
		NewFish = LanternFish(int(counter))
		FishObjects.append(NewFish)

	for i in range(0, Days):

		#print("\n---------------", len(FishObjects))
		#foo = []
		#for _, Fishy in enumerate(FishObjects):
		#	foo.append(Fishy.Counter)
		#print(foo)

		for i in range(0, len(FishObjects)):
			FishObjects[i].Age()

		

	return len(FishObjects)

print(Main())