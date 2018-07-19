from tkinter import*
from DinoGame import Dino, Game
from NeuralNetwork import NeuralNetwork
from GeneticAlgorithm import GeneticAlgorithm
import numpy as np

#TODO: Add neural network display
#
#Pop size, gen
settings = [5, 1]
rootLoop = True
dinos = []
nn = []
fitData = []

tk = Tk()
genDisplay = StringVar()
scoreDisplay = StringVar()
genDisplay.set("Generation: 1")
scoreDisplay.set("Score: 0")

gameCanvas = Canvas(tk, width = 600, height = 250)
genLabel = Label(tk, textvariable=genDisplay)
scoreLabel = Label(tk, textvariable=scoreDisplay)

genLabel.grid(column = 0, row = 0)
scoreLabel.grid(column = 1, row = 0)
gameCanvas.grid(column = 0, row = 1, columnspan = 2)

for x in range(settings[0]): 
	dinos.append(Dino(70, 130, gameCanvas, NeuralNetwork([4, 5, 1])))
	nn.append(dinos[x].nn)

ga = GeneticAlgorithm()
game = Game(gameCanvas, 170, dinos)

def quitFunc():
	global rootLoop
	rootLoop = False


tk.protocol('WM_DELETE_WINDOW', quitFunc)

while rootLoop:
	for x in dinos: x.update()
	game.update()
	#

	if game.gameLoop == False:
		fitData = []
		for y in dinos:
			fitData.append(y.getScore())
		newGen = ga.createNewGeneration(settings[0], fitData, nn)
		for x in range(0, settings[0]):
			dinos[x].newGen(newGen[x])
		game.reset()
		settings[1] += 1
		print("Gen: {}".format(settings[1]))
		genDisplay.set("Generation: {}".format(settings[1]))

	scoreDisplay.set("Score: {}".format(int(round(game.score, 0))))
	tk.update_idletasks()
	tk.update()

tk.destroy()
quit()