import pygame
import random
pygame.init()
pygame.mixer.init()
num = random.randint(0, 10)
palpite = 0
adv = -1
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
while adv != num:
    adv = int(input('Adivinhe o número que pensei de 0 a 10: '))
    if adv == num:
        print(' PARABÉNS!!! Você acertou! ')
        print('voce precisou de {} palpites para acertar'.format(palpite))
        pygame.mixer.music.load('ex 028.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(1)
        break
        print('voce precisou de {} palpites para acertar'.format(palpite))
    else:
        palpite += 1
        print(' Você errou! Tente novamente.')
        pygame.mixer.music.load('ex 021.mp3')
        pygame.mixer.music.play()
        print('Você está no {}o. palpite'.format(palpite))
pygame.quit()
