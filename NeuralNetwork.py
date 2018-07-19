#Code adapted from http://neuralnetworksanddeeplearning.com/chap1.html
#Currently, some code isn't functional for the neural network, specifically biases. Being worked on.

#FIXME: Add biases to the neural network

import numpy as np
class NeuralNetwork():
    def __init__(self, size):
        #Initializes Neural Network. Can init with previous NN data
        self.size = size
        #self.biases = [(np.random.randn(x, 1)) for x in self.size[1:]]
        self.weights = [(np.random.randn(y, x)) for x, y in zip(self.size[:-1], self.size[1:])]
        #print(self.biases)

    def sigmoid(self, z):
        return(1.0/(1.0+np.exp(-z)))

    def returnOutput(self, a):
        #returns the output of the neural network (currently biases are not working. Will be fixed in the future)
        #for b, w in zip(self.biases, self.weights):
        for w in self.weights:
            a = self.sigmoid(np.dot(w, a))
        return(a)

    def mutate(self):
        #changes 1 weight and 1 bias value
        x = np.random.randint(0, len(self.weights))
        y = np.random.randint(0, len(self.weights[x]))
        z = np.random.randint(0, len(self.weights[x][y]))
        self.weights[x][y][z] += 1 * np.random.random() - 0.5
        #print("{} {} {}".format(x, y, z))
        #x = np.random.randint(0, len(self.biases))
        #y = np.random.randint(0, len(self.biases[x]))
        #z = np.random.randint(0, len(self.biases[x][y]))
        #self.biases[x][y][z] += 1 * np.random.random() - 0.5

    def saveNeuralNetwork(self):
        #returns mutated neural network data. Can be fed into a new neural network.
        #return(self.weights + self.biases)
        self.mutate()
        return(self.weights)

    def modifyNetwork(self, newNet):
        self.weights = newNet


if __name__ == '__main__':
    nn = NeuralNetwork([2, 3, 1])
    print(nn.returnOutput([1, 2]))
   

