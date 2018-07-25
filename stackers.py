from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
import random

sense = SenseHat()
sense.clear()

class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480))
		self.gaming = True

	def startGame(self):
		x=0
		y=7

		pygame.time.set_timer(USEREVENT +1, 400)
		while self.gaming:
			for event in pygame.event.get():
		 		if  event.type == KEYDOWN:
					s = random.randint(1, 255)
					n = random.randint(0, 255)
					p = random.randint(1, 255)
					sense.set_pixel(x, y, (s, p, n))			
					x = 0
					y = y - 1
					if(x == 8):
						x = 0
				else:
					sense.set_pixel(x, y, (0, 0, 255))
					time.sleep(0.3)
					sense.set_pixel(x, y, (0, 0, 0))
					x = x + 1	
					if(x == 8):
						x = 0
						
					

if __name__ == "__main__":
	try:
		game = stack()
		game.startGame()
	
	except KeyboardInterrupt:
		sense.clear()

