from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MovePlayerAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        player = cast.get_first_actor(PLAYER_GROUP)
        body = player.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - PLAYER_WIDTH):
            position = Point(SCREEN_WIDTH - PLAYER_WIDTH, position.get_y())
            
        body.set_position(position)
        