from src.Dependencies import *
from src.constants import *
class ObjectConf:
    def __init__(self, type, img, frame, solid, default_state, states, width, height):
        self.type = type
        self.image = img
        self.frame = frame
        self.solid = solid
        self.default_state = default_state
        self.state_list = states
        self.width = width
        self.height = height

#ObjectConf('switch')


GAME_OBJECT_DEFS = {
    'switch': ObjectConf(
        'switch',
        gSwitch_image_list,
        2, 
        False,
        "unpressed", 
        {'unpressed':1, 'pressed':0}, 
        width=48,
        height=48
        ),
    'pot': ObjectConf(
        'pot',
        [gRoom_image_list[POT_IDLE], gRoom_image_list[POT_BREAK]],
        1,
        False,
        "idle",
        {'idle':0, 'break': 1, 'lift': 0},
        width=48,
        height=48
    ),
    'freeheart': ObjectConf(
        'freeheart',
        [gHeart_image_list[2]],
        0,
        False,
        "idle",
        {'idle':0, 'use': 1},
        width=16,
        height=16
    ),
    'star': ObjectConf(
        'star',
        [gStar_image_list],
        0,
        False,
        "idle",
        {'idle':0, 'use': 1},
        width=16,
        height=16
    )
}