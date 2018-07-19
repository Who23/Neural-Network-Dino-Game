import numpy as np
class GeneticAlgorithm():
	def __init__(self):
		self.fitnesses = []

	def createNewGeneration(self, size, fitnesses, nn):
		self.fitnesses = fitnesses
		self.fitnesses.sort(reverse = True)
		fitnessSize = sum(self.fitnesses)
		newgen = []
		for _ in range(size):
			pickedNum = np.random.randint(1, fitnessSize + 1)
			for pos, _ in enumerate(self.fitnesses):
				if pickedNum <= sum(self.fitnesses[:pos]):
					break
				newgen.append(nn[pos].saveNeuralNetwork())
		return(newgen)