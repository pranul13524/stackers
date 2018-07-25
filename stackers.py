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
			for event in pygame.event.get():
		 		if  event.type == KEYDOWN:
					sense.set_pixel(column - 1, 7, (0, 255, 255))
					self.gaming = False
				else:
					sense.set_pixel(x, 7, (0, 0, 255))
					time.sleep(0.3)
					sense.set_pixel(x, 7, (0, 0, 255))
					sense.clear()
					x = x + 1
					if(x == 8):
						x = 0


if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	
	except KeyboardInterrupt:
		sense.clear()

