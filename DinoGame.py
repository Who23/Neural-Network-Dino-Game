#Currently, this game does not work independently of the main.py. This is being worked on.
#TODO: Make dino game modular
class Dino():
	def __init__(self, x, y, canvas, nn):
		self.c = canvas
		self.by = y
		self.y = y
		self.yvel = 0
		self.grounded = True
		#self.id = c.create_image(self.x, self.y, image = img, anchor = tk.NW)
		self.id = self.c.create_rectangle(0 , 0, 20, 40)
		self.c.move(self.id, x, y)
		self.score = 0
		self.inputs = []
		self.nn = nn
		self.alive = True

	def move(self, event = None):
		#jump
		if self.grounded:
			self.grounded = False
			self.yvel = -7

	def update(self):
		if self.alive == True:
			#update function that does jumping
			self.y += int(self.yvel)
			self.yvel += 0.28
			if self.y > self.by:
				self.y = self.by
				self.yvel = 0
				self.grounded = True

			#Move the dino to it's real y-value
			self.c.move(self.id, 0, self.y - self.c.coords(self.id)[1])

			if self.inputs != []:
				if self.nn.returnOutput(self.inputs)[0] >= 0.5:
					self.move()


	def getScore(self):
		return(self.score)

	def writeScore(self, score):
		#sets score for dino, and moves tkinter dino off-screen.
		self.score = score
		self.alive = False
		self.c.move(self.id, 0, -200)


	def getDemSTATS(self, stats):
		#gets stats for neural network
		self.inputs = stats

	def newGen(self, newNN):
		#resets dino
		self.nn.modifyNetwork(newNN)
		self.alive = True
		self.c.move(self.id, 0, -130)


class Game():
	def __init__(self, canvas, base_height, dinoObj):
		self.c = canvas
		self.speed = 4
		self.acc = 1.00005
		self.cacti = []
		self.c.create_line(60, base_height, 540, base_height)
		self.bh = base_height
		self.score = 0
		self.dinoObjs = dinoObj
		self.dinos = [x.id for x in self.dinoObjs] #dino canvas ids
		self.gameLoop = True
		self.counter = 0

	def hitboxDetection(self):
		#Hitbox detection
		#FIXME: Make sure that hitbox detection works when screen is resized
		for x in range(len(self.dinos)):
			if x != "":
				for y in self.cacti:
					if ((self.c.coords(y)[0] <= self.c.coords(self.dinos[x])[0] + 20) and (self.c.coords(self.dinos[x])[0] + 20 <= self.c.coords(y)[0] + 20)) or ((self.c.coords(y)[0] <= self.c.coords(self.dinos[x])[0]) and (self.c.coords(self.dinos[x])[0] <= self.c.coords(y)[0] + 20)):
						if (self.c.coords(y)[1] <= self.c.coords(self.dinos[x])[1] + 40) and (self.c.coords(self.dinos[x])[1] + 40 <= self.c.coords(y)[1] + 30):
							#If touching, sends score to the dino, and deletes the dino from the game
							self.dinoObjs[x].writeScore(self.score)
							self.dinos[x] = ""

		#Deletes the dinos, and ends game if none are left
		self.dinos[:] = (value for value in self.dinos if value != "")
		if self.dinos == []:
			self.gameLoop = False

	def update(self):
		#Checks for gameloop
		if self.gameLoop == True:
			self.score += 0.01 * self.speed
			#Max speed
			if self.speed < 200:
				self.speed *= self.acc
			#Sets up cactis if none are on screen
			if self.cacti == []:
				self.cacti.append(self.c.create_rectangle(520, self.bh - 30, 540, self.bh))

			#Moves the cactus, and moves the cactus back to the front, to be moving again
			for x in self.cacti:
				self.c.move(x, -self.speed, 0)
				if self.c.coords(x)[0] < 50:
					self.c.move(x, 520 - self.c.coords(x)[0], 0)
					self.counter += 1

			self.cacti.insert(self.cacti[len(self.cacti) - 1], self.cacti.pop(0))

			self.hitboxDetection()

			#Feed dinos nn data. [Ditance to cactus, speed, cactus width, cactus height]
			for x in self.dinoObjs:
				x.getDemSTATS([self.c.coords(self.cacti[0])[0] - self.c.coords(x.id)[0], self.speed, 20, 30])




	def reset(self):
		#Resets game to play again
		self.speed = 4
		self.dinos = [x.id for x in self.dinoObjs]
		self.score = 0
		for x in self.cacti:
			self.c.move(x, 520 - self.c.coords(x)[0], 0)
		self.gameLoop = True


# def quitFunc(event):
# 	tk.destroy()
# 	quit()



# if __name__ == '__main__':
# 	tk = Tk()
# 	c = Canvas(tk, width = 600, height = 250)
# 	c.pack()

# 	dino = Dino(70, 130, c)
# 	game = Game(c, 170, [dino])

# 	tk.bind("<=>", lambda event: quitFunc(event))
# 	tk.bind("<Key>", lambda event: dino.move(event))
# 	tk.bind("</>", lambda event: dino.debug(event))
# 	tk.bind("a", lambda event: game.reset(event, [dino]))

# 	while True:
# 		dino.update()
# 		game.update()
# 		tk.update_idletasks()
# 		tk.update()