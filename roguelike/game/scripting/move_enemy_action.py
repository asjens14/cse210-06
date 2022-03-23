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
            print(velocity.get_x())
            bricks = cast.get_actors(BRICK_GROUP)

            for brick in bricks:
                brick_body = brick.get_body()
                points = brick.get_points()
                if points == "1":
                    if self._physics_service.has_collided(body, brick_body):
                        enemy.bounce()
                        # sound = Sound(BOUNCE_SOUND)
                        # self._audio_service.play_sound(sound)

