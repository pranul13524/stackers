from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True

	def startGame(self):
		x=0
		pygame.time.set_timer(USEREVENT +1, 800)
		while self.gaming:
			while x<8:
	
						sense.set_pixel(x, 7, (0, 0, 255))
						time.sleep(0.2)
						sense.set_pixel(x, 7, (0, 0, 255))
						time.sleep(0.05)
						x = x + 1
			x = 0


if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
		loop()
	except KeyboardInterrupt:
		sense.clear()
