from constants import *
from game.scripting.action import Action


class MoveBallAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        if cast.get_actors(BALL_GROUP) is not None:
            balls = cast.get_actors(BALL_GROUP)
            for ball in balls:
                body = ball.get_body()
                position = body.get_position()
                velocity = body.get_velocity()
                position = position.add(velocity)
                body.set_position(position)
        
        if cast.get_actors(ENEMY_BALL_GROUP) is not None:
            eballs = cast.get_actors(ENEMY_BALL_GROUP)
            for eball in eballs:
                body = eball.get_body()
                position = body.get_position()
                velocity = body.get_velocity()
                position = position.add(velocity)
                body.set_position(position)

        else:
            pass
