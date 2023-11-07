import pygame, math, random, sys, os
from src.constants import *

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
music_channel = pygame.mixer.Channel(0)
music_channel.set_volume(0.2)

from src.Dependencies import *



class GameMain:
    def __init__(self):

        self.max_frame_rate = 60
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        #self.sprite_collection = SpriteManager().spriteCollection

        self.g_state_manager = StateMachine(self.screen)

        states = {
            'start': StartState(self.g_state_manager),
            'play': PlayState(self.g_state_manager),
            'game_over': GameOverState(self.g_state_manager),
        }

        self.g_state_manager.SetStates(states)



    def PlayGame(self):
        gSounds['music'].play(-1)
        clock = pygame.time.Clock()

        self.g_state_manager.Change("start")

        while True:
            pygame.display.set_caption("Zelda game running with {:d} FPS".format(int(clock.get_fps())))
            dt = clock.tick(self.max_frame_rate) / 1000.0

            events = pygame.event.get()

            self.g_state_manager.update(dt, events)

            self.screen.fill((0, 0, 0))
            self.g_state_manager.render()

            pygame.display.update()


if __name__ == '__main__':
    main = GameMain()
    main.PlayGame()



