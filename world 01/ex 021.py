import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex 021.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit() 