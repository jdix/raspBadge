#/bin/python 

#REPLACE ALL OF THIS WITH THE REAL IMPLEMENTATION
import pygame
class Sound:
	def playRFID(self):
		self.play("beep1.ogg")
	def playError(self):
		self.play("badswap.wav")
	def playSuccess(self):
		self.play("match5.wav")

	def play (self, filename):
		sound_file = "/home/pi/raspBadge/pi/sound/" + filename
		pygame.mixer.init(44100, -16, 1, 1024)
		sound = pygame.mixer.Sound(sound_file)
		sound.play(loops = 1)
