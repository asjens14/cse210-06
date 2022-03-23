from constants import *
from game.scripting.action import Action


class ControlPlayerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        if self._keyboard_service.is_key_down(LEFT) or self._keyboard_service.is_key_down(LEFT2): 
            player.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT) or self._keyboard_service.is_key_down(RIGHT2): 
            player.swing_right()
        elif self._keyboard_service.is_key_down(UP) or self._keyboard_service.is_key_down(UP2): 
            player.swing_up()
        elif self._keyboard_service.is_key_down(DOWN) or self._keyboard_service.is_key_down(DOWN2): 
            player.swing_down()   
        else: 
            player.stop_moving()        