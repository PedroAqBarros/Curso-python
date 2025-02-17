import pygame
import random
pygame.init()
pygame.mixer.init()
num = random.randint(0, 5)
while True:
    adv = int(input('Adivinhe o número que pensei de 0 a 5: '))
    if adv == num:
        print(' PARABÉNS!!! Você acertou! ')
        pygame.mixer.music.load('ex 028.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        break
    else:
        print(' Você errou! Tente novamente.')
        pygame.mixer.music.load('ex 021.mp3')
        pygame.mixer.music.play()

pygame.quit()
