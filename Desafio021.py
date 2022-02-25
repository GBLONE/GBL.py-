# Tocando uma música .mp3
import pygame
pygame.init()
pygame.mixer.music.load('abc021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
