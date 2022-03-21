from constants import *
from game.scripting.action import Action


class MoveEnemyAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        enemies = cast.get_actors(ENEMY_GROUP)
        
        for enemy in enemies:
            body = enemy.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
