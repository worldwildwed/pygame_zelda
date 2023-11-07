from src.states.BaseState import BaseState
import pygame, sys
from src.Dependencies import *
from src.constants import *
from src.entity_defs import *

from src.entity_defs import EntityConf
from src.Player import Player

from src.states.entity.player.PlayerWalkState import PlayerWalkState
from src.states.entity.player.PlayerIdleState import PlayerIdleState
from src.states.entity.player.PlayerAttackState import PlayerAttackState
from src.StateMachine import StateMachine

from src.world.Dungeon import Dungeon

class PlayState(BaseState):
    def __init__(self, state_machine):
        super(PlayState, self).__init__(state_machine)

    def Enter(self, params):
        entity_conf = ENTITY_DEFS['player']
        self.player = Player(entity_conf)
        self.dungeon = Dungeon(self.player)

        self.player.state_machine = StateMachine(pygame.display.get_surface())
        self.player.state_machine.SetStates({
            'walk': PlayerWalkState(self.player, self.dungeon),
            'idle': PlayerIdleState(self.player),
            'swing_sword': PlayerAttackState(self.player, self.dungeon),
        })

        self.player.ChangeState('walk')

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        self.dungeon.update(dt, events)

        if self.player.health == 0:
            self.state_machine.Change('game_over')

        #temp
        #self.room.update(dt, events)

    def render(self, screen):
        # dungen render including Room render
        self.dungeon.render(screen)

        # Render Health Bar
        health_left = self.player.health
        for i in range(10):
            if health_left > 1:
                heart_frame = 2
            elif health_left ==1:
                heart_frame = 1
            else:
                heart_frame = 0

            screen.blit(gHeart_image_list[heart_frame], (i * (TILE_SIZE+3), 6))
            health_left -=2

        if self.player.shielded:
              screen.blit(gShieldHeart_image_list, (10 * (TILE_SIZE+3), 6))
        #temp
        #self.room.render(screen)


    def Exit(self):
        pass

